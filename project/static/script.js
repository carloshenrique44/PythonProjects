function scrollProjects(direction) {
    const carousel = document.getElementById('projectsCrousel');
    const scrollAmount = 400;
    carousel.scrollBy({
        left: direction * scrollAmount,
        behavior: 'smooth'
    });
}