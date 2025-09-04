var EOChatControl={value:""};
	var conf;

	var mensagemFinal;
	
	function receiveMessage(messageObject) {
	const mensagem = JSON.parse(messageObject);

	if ({{idchat}} === mensagem.conversa) {
		const chatBox = document.querySelector(".chat-box");
		const chatDiv = document.createElement("div");
		chatDiv.className = "chat-l";

		const messDiv = document.createElement("div");
		messDiv.className = "messleft";
		messDiv.id = mensagem.id;

		const nomeDiv = document.createElement("div");
		nomeDiv.className = "nomeleft";
		nomeDiv.innerHTML = `<strong>${mensagem.nomeDestinatario}</strong>`;

		if (mensagem.tipo === 4) {
			messDiv.innerHTML = `<p>${mensagem.conteudo}</p><img onclick="window.open('${mensagem.anexos[0].action}','targetWindow','width=800, height=600')" src="${mensagem.anexos[0].link}" style="max-width:200px; cursor: pointer;"/>`;
		} else if (mensagem.tipo === 11) {
			messDiv.innerHTML = `<p>${mensagem.conteudo}</p><video controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></video>`;
		} else if (mensagem.tipo === 12) {
			messDiv.innerHTML = `<p>${mensagem.conteudo}</p><audio controls style="max-width: 200px;"><source src="${mensagem.anexos[0].link}"></audio>`;
		} else if (mensagem.tipo === 13) {
			messDiv.innerHTML = `<p>${mensagem.conteudo} <a href="${mensagem.anexos[0].link}" target="_blank" download><i class="fa-solid fa-link"></i></a></p>`;
		} else {
			messDiv.innerHTML = `<p>${mensagem.conteudo}</p>`;
		}

		const dataDiv = document.createElement("div");
		dataDiv.className = "data";
		dataDiv.innerText = formatarHora(mensagem.data);

		const dotIcon = document.createElement("i");
		dotIcon.className = "fas fa-ellipsis-v";
		dotIcon.style.cursor = "pointer"; 

		nomeDiv.appendChild(dotIcon);
		messDiv.prepend(nomeDiv);
		messDiv.appendChild(dataDiv);

		chatDiv.appendChild(messDiv);
		chatBox.appendChild(chatDiv);
	}
}

	function sendMessage() {
		if ($("#message-itens").data("sending")) {
			return;
		}
	
		$("#message-itens").data("sending", true);
	
		let msg = $("#message-itens").val().trim();
		let replyTo = $("#inputSend").data("replyingTo");
	
		if (msg.length > 0) {
			mensagemFinal = msg;
			
			if (replyTo) {
				mensagemFinal = `
				<div class="reply-box">
				<p class="reply-name"><strong>${replyTo.nome}</strong></p>
				<p class="reply-text">${replyTo.mensagem}</p>
				</div>
				<p>${msg}</p>
				`;
				
				var JsonMsg = { 
					ContentMessage_TX : msg,
					tInt_reply_ID : replyTo.idInteracao
				};
				
				EOChatControl.value = JSON.stringify(JsonMsg, null, 2);
			} else {
				var JsonMsg = { 
					ContentMessage_TX : msg
				};
			
				EOChatControl.value = JSON.stringify(JsonMsg, null, 2);
			}
	
			gx.fx.obs.notify("EOChatControl.getValue")
			gx.fx.obs.notify("EOChatControl.onSendMessage");
	
		}
	
		else {
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
		messDiv.innerHTML = `<p>${message}</p>`;
		messDiv.id = id;
		dataDiv.className = "data";
		dataDiv.innerText = formatarHora(dataMensagem) + " ";
		dataDiv.appendChild(statusIcon);
		nomeDiv.appendChild(dotIcon);
		messDiv.prepend(nomeDiv);
		messDiv.appendChild(dataDiv);
		chatDiv.appendChild(messDiv);
		chatBox.appendChild(chatDiv);
		dotIcon.className = "fas fa-ellipsis-v";
		nomeDiv.appendChild(dotIcon);
	}
	
	function renderSentFile(id, filename, type, url){
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
		} else if(type === 13) {
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

	function AddEventListener(){
		var inputText = document.getElementById("message-itens");
		
		$("#message-itens").off("keydown").on("keydown", function(event) {
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
					EOChatControl.value = `{"filename": "${event.target.files[0].name}", "base64": "${reader.result}"}`;
					
					gx.fx.obs.notify("EOChatControl.uploadFile");
				};
			} else {
				console.log('Nenhum arquivo selecionado');
			}
		});
	}
	
	$(document).on('click', 'i.fa-ellipsis-v', function (event) {
		
		console.log('clicoumerda');
		
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
			let mensagem;

			let replyBox = msgContainer.find(".reply-box");
			if (replyBox.length > 0) {
				const clone = msgContainer.clone();
				clone.find(".reply-box").remove();
				mensagem = clone.find("p").text().trim();
			} else {
				mensagem = msgContainer.find("p").text().trim();
			}

			let nomeRemetente = msgContainer.find("strong").first().text().trim();
			let idInteracao = msgContainer.attr('id');
			
			if (!mensagem) {
				if (msgContainer.find("img").length > 0) mensagem = "[Imagem]";
				else if (msgContainer.find("video").length > 0) mensagem = "[Vídeo]";
				else if (msgContainer.find("audio").length > 0) mensagem = "[Áudio]";
				else if (msgContainer.find("a").length > 0) mensagem = "[Arquivo]";
				else mensagem = "[Conteúdo multimídia]";
			}
			
			console.log("Mensagem:", mensagem, "Nome:", nomeRemetente, "ID Interação:", idInteracao);
			
			if (mensagem) {
				$("#reply-text").html(`<strong>${nomeRemetente}</strong><br>${mensagem}`); 
				$("#reply-container").css({
					display: "flex",
					opacity: 1,
					visibility: "visible"
				});
		
				$("#inputSend").data("replyingTo", {
					nome: nomeRemetente,
					mensagem: mensagem,
					idInteracao : idInteracao
				});
			}
			$(".message-options").remove();
		});

		$(document).on("click", function(e) {
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