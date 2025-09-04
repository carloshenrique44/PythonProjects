<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/boxicons/2.1.1/css/boxicons.min.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="container">
<div class="profile">
	<div id="profileHd" class="left">
		<div id="avatar" class="image">
			<img src="https://ui-avatars.com/api/" class="avatar-image">
		</div>
	</div>
	<div id="chatActions" class="right">
		<div class="icon-container" id="drops">
			<div class="icon-box">
				<i class='bx bx-dots-vertical-rounded'></i>
			</div>
			<div id="myDropdown" class="dropdown-content">
				<a id="ActionsFinish" href="#" onclick="finishConversation()">Encerrar conversa</a>
				<a id="ActionsFinishSurvey" href="#" onclick="endWithSurvey()">Encerrar com pesquisa</a>
				<a id="ActionsReturn" href="#" onclick="returnToTheQueue()">Retornar para a fila</a>
				<a id="ActionsTransfer" href="#" onclick="transferToUser()">Transferir</a>
				<a id="ActionsStandby" href="#" onclick="standBy()">Stand-by</a>
				<a id="ActionsDownloadPDF" href="#" onclick="downloadPDF()">Baixar em PDF</a>
			</div>
		</div>
	</div>
</div>
<div id="line">
	<hr>               
</div>
<div id="chatcontainer"  {{OpenAsChatCorner?}}style="height:calc(100vh - 300px);"{{/OpenAsChatCorner}}>
	<div id="chat" class="chat-box"></div>
	
	<div id="endMessagesContainer" class="toEndMessagesList">
		<div id="endMessagesButton" class="btn paginateButton">
			<i class="fa-solid fa-arrow-down"></i>
		</div>
	</div>
</div>
<div id="reply-container" class="reply-container">
    <span class="close-reply">X</span>
    <p id="reply-text"></p>
</div>

<div id="inputSend" class="mensagem">
	<textarea id="message-itens" placeholder="Digite sua mensagem"></textarea>
</div>
<div id="sendActions" class="chat-footer">
	<div class="icon-message">
		<div onclick="document.getElementById('file').click()" class="icon-box-footer icon-chat">
			<i class="bx bx-link-alt">
				<input type="file" name="file" id="file" style="display:none;">
			</i>
		</div>
		<div onclick="sendMessage()" class=" icon-box-footer icon-chat">
			<i class="bx bx-send"></i>
		</div>
	</div>
</div>

<script>	
	var EOChatControl = { value: "" };
	var conf;
	let nomeUsuarioAtual = "";
	let userIsAtBottom = true;
	
	var mensagemFinal;
	
	function receiveMessage(messageObject) {
		const mensagem = JSON.parse(messageObject);
		
		if (conf.tConv_ID === mensagem.conversa) {
			const chatBox = document.querySelector(".chat-box");
			const chatDiv = document.createElement("div");
			chatDiv.className = "chat-l";
	
			const messDiv = document.createElement("div");	
			messDiv.className = "messleft";
			messDiv.id = mensagem.id;
	
			const nomeDiv = document.createElement("div");
			nomeDiv.className = "nomeleft";
			nomeDiv.style.display = "flex";
			nomeDiv.style.alignItems = "center";
			nomeDiv.style.justifyContent = "space-between";
	
			const strongNome = document.createElement("strong");
			strongNome.textContent = mensagem.nomeDestinatario;
	
			const dotIcon = document.createElement("i");
			dotIcon.className = "fas fa-ellipsis-v message-options-icon";
	
			nomeDiv.appendChild(strongNome);
			nomeDiv.appendChild(dotIcon);
			messDiv.appendChild(nomeDiv);
	
			let conteudoHtml = "";
			if (mensagem.tipo === 4) {
				conteudoHtml = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><img onclick="window.open('${mensagem.anexos[0].action}','targetWindow','width=800, height=600')" src="${mensagem.anexos[0].link}" style="max-width:200px; cursor: pointer;"/>`;
			} else if (mensagem.tipo === 11) {
				conteudoHtml = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><video controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></video>`;
			} else if (mensagem.tipo === 12) {
				conteudoHtml = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><audio controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></audio>`;
			} else if (mensagem.tipo === 13) {
				conteudoHtml = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo} <a href="${mensagem.anexos[0].link}" target="_blank" download><i class="fa-solid fa-link"></i></a></p>`;
			} else {
				conteudoHtml = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p>`;
			}
	
			messDiv.innerHTML += conteudoHtml;
	
			const dataDiv = document.createElement("div");
			dataDiv.className = "data";
			dataDiv.innerText = formatarHora(mensagem.data);
			messDiv.appendChild(dataDiv);
	
			chatDiv.appendChild(messDiv);
			chatBox.appendChild(chatDiv);
			NewMessageAdd();
		}
	}

	
	function sendMessage() {
		if ($("#message-itens").data("sending")) 
			return;
	
		$("#message-itens").data("sending", true);
	
		let msg = $("#message-itens").val().trim();
		let replyTo = $("#inputSend").data("replyingTo");
	
		if (msg.length > 0) {
			mensagemFinal = msg;
	
			if (replyTo) {
				const nomeParaMostrar = replyTo.nome === nomeUsuarioAtual ? "Você" : replyTo.nome;
	
				mensagemFinal = `
				<div class="reply-box">
				<p class="reply-name"><strong>${nomeParaMostrar}</strong></p>
				<p class="reply-text">${replyTo.mensagem}</p>
				</div>
				<p>${msg}</p>
				`;
	
				var JsonMsg = {
					ContentMessage_TX: msg,
					tInt_reply_ID: replyTo.idInteracao
				};
	
				EOChatControl.value = JSON.stringify(JsonMsg, null, 2);
			} else {
				mensagemFinal = `<p style="white-space: pre-line; margin: 0;">${msg}</p>`;
				var JsonMsg = {
					ContentMessage_TX: msg
				};
	
				EOChatControl.value = JSON.stringify(JsonMsg, null, 2);
			}
	
			gx.fx.obs.notify("EOChatControl.getValue");
			gx.fx.obs.notify("EOChatControl.onSendMessage");
			
		} else {
			$("#message-itens").removeData("sending");
			$("#message-itens").removeData("messageSent");
		}
	}
	
	function renderSentMessage(id, message) {
		if (mensagemFinal) {
			message = mensagemFinal;
			mensagemFinal = null;
	
			if (!$("#message-itens").data("messageSent")) {
				setTimeout(() => {
					$("#message-itens").removeData("sending");
					$("#message-itens").data("messageSent", true);
					$("#message-itens").removeData("messageSent");
				}, 2000);
			}
	
			$("#reply-container").hide();
			$("#inputSend").removeData("replyingTo");
			$("#message-itens").val('');
		}
	
		const chatBox = document.querySelector(".chat-box");
		const chatDiv = document.createElement("div");
		const messDiv = document.createElement("div");
		const dataDiv = document.createElement("div");
		const statusIcon = document.createElement("i");
		const nomeDiv = document.createElement("div");
		const dotIcon = document.createElement("i");
		const dataMensagem = new Date();
	
		statusIcon.className = "fa-solid fa-check";
		chatDiv.className = "chat-r";
		messDiv.className = "mess";
		messDiv.innerHTML = message;
		messDiv.id = id;
	
		dataDiv.className = "data";
		dataDiv.innerText = formatarHora(dataMensagem) + " ";
		dataDiv.appendChild(statusIcon);
	
		nomeDiv.appendChild(dotIcon);
		messDiv.prepend(nomeDiv);
		messDiv.appendChild(dataDiv);
		chatDiv.appendChild(messDiv);
		chatBox.appendChild(chatDiv);
		NewMessageAdd();
		dotIcon.className = "fas fa-ellipsis-v";
		nomeDiv.appendChild(dotIcon);
	}

	
	function renderSentFile(id, filename, type, url) {
		const chatBox = document.querySelector(".chat-box");
		const chatDiv = document.createElement("div");
		const messDiv = document.createElement("div");
		const dataDiv = document.createElement("div");
		const statusIcon = document.createElement("i");
		const nomeDiv = document.createElement("div");
		const dotIcon = document.createElement("i");
		const dataMensagem = new Date();
	
		statusIcon.className = "fa-solid fa-check";
		chatDiv.className = "chat-r";
		messDiv.className = "mess";
	
		if (type === 4) {
			messDiv.innerHTML = `<img onclick="window.open('${url}','targetWindow','width=800, height=600')" src="${url}" style="max-width:200px; cursor: pointer;"/>`;
		} else if (type === 11) {
			messDiv.innerHTML = `<video controls style="max-width: 200px;"><source src="${url}"></video>`;
		} else if (type === 12) {
			messDiv.innerHTML = `<audio controls style="max-width: 200px;"><source src="${url}"></audio>`;
		} else if (type === 13) {
			messDiv.innerHTML = `<p>${filename} <a href="${url}" target="_blank" download><i style="color: #049cc3;" class="fa-solid fa-link"></i></a></p>`;
		}
	
		messDiv.id = id;
		dataDiv.className = "data";
		dataDiv.innerText = formatarHora(dataMensagem) + " ";
		dataDiv.appendChild(statusIcon);
		messDiv.prepend(nomeDiv);
		messDiv.appendChild(dataDiv);
		chatDiv.appendChild(messDiv);
		chatBox.appendChild(chatDiv);
		NewMessageAdd();
	}
	
	function formatarData(dataString) {
		const data = new Date(dataString);
		return `${data.getDate().toString().padStart(2, '0')}/${(data.getMonth() + 1).toString().padStart(2, '0')}/${data.getFullYear()}`;
	}
	
	function replyToMessage(nome, mensagem) {
		$("#message-itens").data("replyingTo", { nome: nome, mensagem: mensagem });
		$("#reply-text").html(`<strong>${nome}:</strong> ${mensagem}`);
		$("#reply-container").css({
			display: "block",
			opacity: 1,
			visibility: "visible"
		});
	}
	
	function formatarHora(dataString) {
		const data = new Date(dataString);
		return `${data.getHours().toString().padStart(2, '0')}:${data.getMinutes().toString().padStart(2, '0')}`;
	}
	
	function AddEventListener() {
		var inputText = document.getElementById("message-itens");
	
		$("#message-itens").off("keydown").on("keydown", function (event) {
			if (event.key === "Enter" && !event.repeat) {
				event.preventDefault();
				if (!$(this).data("sent")) {
					$(this).data("sent", true);
					sendMessage();
					setTimeout(() => $(this).removeData("sent"), 500);
				}
			}
		});
	
		var fileInput = document.getElementById('file');
	
		fileInput.addEventListener('change', (event) => {
			/* Obtém os arquivos selecionados */
			const files = event.target.files;
	
			/* Verifica se há arquivos selecionados */
			if (files.length > 0) {
				var reader = new FileReader();
				reader.readAsDataURL(files[0]);
				reader.onload = function () {
					EOChatControl.value = `{"filename": "${retirarCaracteresEspeciais(event.target.files[0].name)}", "base64": "${reader.result}"}`;
	
					gx.fx.obs.notify("EOChatControl.uploadFile");
				};
			} else {
				console.log('Nenhum arquivo selecionado');
			}
		});
	}
	
	function main(messageObject, config, hasMoreMessages) {
		const listaMensagens = JSON.parse(messageObject);
		conf = JSON.parse(config);
		
		const nomeUsuario = listaMensagens[0]?.nomeDestinatario;
		const protocol = conf.tConv_Prot_SL;
		const status = conf.tConv_Stats_CK;
		const phone = conf.PhoneWithoutMask;
		const nomeUsuarioAtual = conf.tUsua_Nome_SL?.trim() || "";
		
		let avatarContainer = document.getElementById("avatar");
		avatarContainer.innerHTML = '';
		
		if (nomeUsuario) {
			let elmAvatar = document.createElement("img");
			elmAvatar.src = `https://ui-avatars.com/api/?background=random&name=${nomeUsuario}`;
			elmAvatar.className = 'avatar-image';
			avatarContainer.appendChild(elmAvatar);
			
			let person = document.createElement("div");
			person.innerHTML = nomeUsuario + ' | ' + protocol;
			let profileHeader = document.getElementById("profileHd");
			profileHeader.appendChild(person);
			let personPhone = document.createElement("div");
			personPhone.innerHTML = phone;
			profileHeader.appendChild(personPhone);
		}
		
		const chatBox = document.querySelector(".chat-box");
		chatBox.innerHTML = '';
		let ultimaData = '';
		
		const prevMessagesContainer = document.createElement("div");
		prevMessagesContainer.id = "nextPageContainer";
		prevMessagesContainer.style.display = "flex";
		prevMessagesContainer.style.justifyContent = "center";
		prevMessagesContainer.style.width = "100%";
		prevMessagesContainer.style.padding = "20px 15px";
		
		const prevMessagesButton = document.createElement("div");
		prevMessagesButton.id = "previousPageButton";
		prevMessagesButton.textContent = "Carregar mensagens Anteriores";
		prevMessagesButton.style.display = "visible";
		
		if (!hasMoreMessages) {
			prevMessagesButton.style.visibility = "hidden";
		}
		
		prevMessagesButton.classList.add("btn", "paginateButton");
		prevMessagesContainer.appendChild(prevMessagesButton);
		
		prevMessagesButton.addEventListener("click", () => {
			backPage();
		});
		
		const endMessagesButton = document.getElementById("endMessagesButton");
		endMessagesButton.addEventListener("click", () => {
			toBottomPage();
		});
		
		chatBox.appendChild(prevMessagesContainer);
		
		for (let i = 0; i < listaMensagens.length; i++) {
			const mensagem = listaMensagens[i];
			const chatDiv = document.createElement("div");
			const messDiv = document.createElement("div");
			const dataDiv = document.createElement("div");
			const nomeDiv = document.createElement("div");
			const dataMensagem = formatarData(mensagem.data);
			
			if (dataMensagem !== ultimaData) {
				const dataTopo = document.createElement("div");
				dataTopo.className = "data-topo";
				dataTopo.innerText = dataMensagem;
				chatBox.appendChild(dataTopo);
				ultimaData = dataMensagem;
			}
			
			if (mensagem?.tipoMensagem == 1) {
				chatDiv.className = "chat-l";
				messDiv.className = "messleft";
				nomeDiv.className = "nomeleft";
				nomeDiv.innerHTML = `<strong>${mensagem.nomeDestinatario}</strong>`;
				
				if (mensagem.tipo === 4) {
					messDiv.innerHTML = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><img onclick="window.open('${mensagem.anexos[0].action}','targetWindow','width=800, height=600')" src="${mensagem.anexos[0].link}" style="max-width:200px; cursor: pointer;"/>`;
					} else if (mensagem.tipo === 11) {
					messDiv.innerHTML = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><video controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></video>`;
					} else if (mensagem.tipo === 12) {
					messDiv.innerHTML = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><audio controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></audio>`;
					} else if (mensagem.tipo === 13) {
					messDiv.innerHTML = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo} <a href="${mensagem.anexos[0].link}" target="_blank" download><i class="fa-solid fa-link"></i></a></p>`;
					} else {
					messDiv.innerHTML = `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p>`;
				}
				
				dataDiv.className = "data";
				dataDiv.innerText = formatarHora(mensagem.data);
				
				} else {
				chatDiv.className = "chat-r";
				messDiv.className = "mess";
				
				if (conf.tUsua_ID != mensagem.idRemetente) {
					nomeDiv.className = "nomeright";
					
					if (!mensagem.idRemetente || mensagem.idRemetente == 0 || mensagem.idRemetente === "undefined") {
						nomeDiv.innerHTML = `<strong><i class="fa-solid fa-robot"></i> ${mensagem.nomeRemetente}</strong>`;
						} else {
						nomeDiv.innerHTML = `<strong><i class="fa-solid fa-user"></i> ${mensagem.nomeRemetente}</strong>`;
					}
				}
				
				messDiv.innerHTML = '';
				
				if (mensagem.replyMessage.tInt_reply_ID) {
					const nomeAutor = mensagem.replyMessage.NameReplier_SL?.trim() || "";
					const nomeExibido = nomeAutor === nomeUsuarioAtual ? "Você" : nomeAutor;
					
					let replymensagemFinal = `
					<div class="reply-box">
					<p class="reply-name"><strong>${nomeExibido}</strong></p>
					<p class="reply-text">${mensagem.replyMessage.ContentMessage_TX}</p>
					</div>
					`;
					
					messDiv.innerHTML = replymensagemFinal;
				}
				
				if (mensagem.tipo === 4) {
					messDiv.innerHTML += `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><img onclick="window.open('${mensagem.anexos[0].action}','targetWindow','width=800, height=600')" src="${mensagem.anexos[0].link}" style="max-width:200px; cursor: pointer;"/>`;
					} else if (mensagem.tipo === 11) {
					messDiv.innerHTML += `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><video controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></video>`;
					} else if (mensagem.tipo === 12) {
					messDiv.innerHTML += `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p><audio controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></audio>`;
					} else if (mensagem.tipo === 13) {
					messDiv.innerHTML += `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo} <a href="${mensagem.anexos[0].link}" target="_blank" download><i style="color: #049cc3;" class="fa-solid fa-link"></i></a></p>`;
					} else {
					messDiv.innerHTML += `<p style="white-space: pre-line; margin: 0;">${mensagem.conteudo}</p>`;
				}
				
				const statusIcon = document.createElement("i");
				
				if (mensagem?.status === 1) {
					statusIcon.className = "fa-solid fa-check";
					} else if (mensagem?.status === 2) {
					statusIcon.className = "fa-solid fa-check-double";
					} else if (mensagem?.status === 3) {
					statusIcon.className = "fa-solid fa-check-double";
					statusIcon.style.color = "#049CC3";
				}
				
				dataDiv.className = "data";
				dataDiv.innerText = formatarHora(mensagem.data) + " ";
				dataDiv.appendChild(statusIcon);
			}
			
			const dotIcon = document.createElement("i");
			dotIcon.className = "fas fa-ellipsis-v message-options-icon";
			nomeDiv.appendChild(dotIcon);
			messDiv.prepend(nomeDiv);
			messDiv.appendChild(dataDiv);
			messDiv.id = mensagem?.id;
			
			chatDiv.appendChild(messDiv);
			chatBox.appendChild(chatDiv);
		}
		
		document.getElementById("drops").addEventListener("click", function () {
			document.getElementById("myDropdown").classList.toggle("show");
		});
		
		AddEventListener();
		NewMessageAdd();
		
		if ({{ Readonly }} == true) {
			if (status == 2) {
				document.getElementById("sendActions").style.display = "none";
				document.getElementById("inputSend").style.display = "none";
				document.getElementById("drops").style.display = "none";
				} else {
				document.getElementById("sendActions").style.display = "none";
				document.getElementById("inputSend").style.display = "none";
				//document.getElementById("ActionsFinish").style.display = "none";
				document.getElementById("ActionsStandby").style.display = "none";
			}
		}
		
		$("#chat").on("scroll", function () {
			const buttonToEnd = document.getElementById("endMessagesButton")
			const buttonPrevItems = document.getElementById("previousPageButton");
			buttonPrevItems.style.visibility = "visible";
			
			if (this.scrollTop != 0) {
				buttonPrevItems.style.visibility = "hidden";
			}
			
			const isEnd = Math.floor(this.scrollHeight - this.clientHeight - this.scrollTop) <= 1;
			buttonToEnd.style.visibility = isEnd ? "hidden" : "visible";
			userIsAtBottom = isEnd; 
			
		});
	}
	
	function changeStatus(id, status) {
		const parentElement = document.getElementById(id);
		
		/* Localizar o <i> dentro do elemento pai */
		const statusIcon = parentElement.querySelector('.data i');
		
		if (statusIcon) {
			if (status == 1) {
				statusIcon.className = "fa-solid fa-check";
				} else if (status == 2) {
				statusIcon.className = "fa-solid fa-check-double";
				} else if (status == 3) {
				statusIcon.className = "fa-solid fa-check-double";
				statusIcon.style.color = "#049CC3";
			}
		}
	}

	function NewMessageAdd() {
		if (userIsAtBottom) {
			toBottomPage();
		}
	}
	
	function toBottomPage() {
		let el = document.getElementById("chat");
		el.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
	}
	
	function backPage() {
		gx.fx.obs.notify("EOChatControl.backPage");
	}
	
	function finishConversation() {
		gx.fx.obs.notify("EOChatControl.endConversation");
	}
	
	function returnToTheQueue() {
		gx.fx.obs.notify("EOChatControl.returnToTheQueue");
	}
	
	function transferToUser() {
		gx.fx.obs.notify("EOChatControl.transferToUser");
	}
	
	function standBy() {
		gx.fx.obs.notify("EOChatControl.standBy");
	}

	function downloadPDF() {
		gx.fx.obs.notify("EOChatControl.downloadPDF");
	}

	function endWithSurvey() {
		gx.fx.obs.notify("EOChatControl.endWithSurvey");
	}
	
	function retirarCaracteresEspeciais(texto) {
		return texto
			.normalize("NFD")                  /* separa letras e acentos */
			.replace(/[\u0300-\u036f]/g, "")   /* remove acentos */
			.replace(/[^a-zA-Z0-9._-]/g, "-"); /* substitui o restante por hífen (ou remova, se quiser) */
	}
	
	$(document).on('click', 'i.fa-ellipsis-v', function (event) {
	
		const msgContainer = $(this).closest(".mess, .messleft");
	
		if ($("#reply-container").length === 0) {
			$("body").append(`
			<div id="reply-container" class="reply-container" style="display: none;">
			<span class="close-reply">X</span>
			<p id="reply-text"></p>
			</div>
			`);
		}
	
		$(".message-options").remove();
	
		const menu = $('<div class="message-options">Responder</div>');
		const posX = event.pageX;
		const posY = event.pageY;
	
		menu.css({
			position: "absolute",
			top: posY + "px",
			left: posX + "px",
			background: "#fff",
			border: "1px solid #ccc",
			padding: "5px 10px",
			cursor: "pointer",
			"z-index": 1000
		});
	
		$("body").append(menu);
		menu.data("msgContainer", msgContainer);
	
		$(document).off('click', '.message-options').on("click", ".message-options", function () {
			console.log("Evento de reply acionado");
	
			let mensagem = "";
			let nomeRemetente = "";
			
			const nomeDiv = msgContainer.find(".nomeleft, .nomeright").first();
			nomeRemetente = nomeDiv.find("strong").text().trim();
			
			let clone = msgContainer.clone();
			clone.find(".reply-box").remove();
			clone.find(".nomeleft, .nomeright").remove();
			clone.find(".data").remove(); 
			
			mensagem = clone.text().trim();
			
			if (!mensagem) {
				if (msgContainer.find("img").length > 0) mensagem = "[Imagem]";
				else if (msgContainer.find("video").length > 0) mensagem = "[Vídeo]";
				else if (msgContainer.find("audio").length > 0) mensagem = "[Áudio]";
				else if (msgContainer.find("a").length > 0) mensagem = "[Arquivo]";
				else mensagem = "[Mensagem sem texto]";
			}

			const idInteracao = msgContainer.attr('id');
	
			console.log("Mensagem:", mensagem, "Nome:", nomeRemetente, "ID Interação:", idInteracao);
	
			const nomeUsuarioAtual = "{{usuarioLogado}}";
			const nomeExibido = nomeRemetente === nomeUsuarioAtual ? "Você" : nomeRemetente;
	
			if (mensagem) {
				$("#reply-text").html(`<strong>${nomeExibido}</strong><br>${mensagem}`);
				$("#reply-container").css({
					display: "flex",
					opacity: 1,
					visibility: "visible"
				});
	
				$("#inputSend").data("replyingTo", {
					nome: nomeRemetente,
					mensagem: mensagem,
					idInteracao: idInteracao
				});
			}
	
			$(".message-options").remove();
		});
	
		$(document).on("click", function (e) {
			if (!$(e.target).hasClass("fa-ellipsis-v") && !$(e.target).hasClass("message-options")) {
				$(".message-options").remove();
			}
		});
	});
	
	$(document).on("click", ".close-reply", function () {
		$("#reply-container").css({
			display: "none",
			opacity: 0,
			visibility: "hidden"
		});
		$("#inputSend").removeData("replyingTo");
	});

</script>