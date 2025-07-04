document.addEventListener('DOMContentLoaded', function () {
    const installButton = document.getElementById('installButton');
    const modal = document.getElementById('swipeableModal');
    const cancelInstall = document.getElementById('cancelInstall');

    if (!modal) {
        console.error('Element with id "swipeableModal" not found.');
        return;
    }

    const modalContent = modal.querySelector('.modal-content');
    if (!modalContent) {
        console.error('Element ".modal-content" not found inside #swipeableModal.');
        return;
    }

    let startY;

    installButton.onclick = function () {
        modal.classList.add('show');
        document.body.classList.add('modal-open');
        modalContent.classList.add('translate-reset');
    };

    cancelInstall.onclick = function () {
        closeModal();
    };

    modal.addEventListener('touchstart', function (e) {
        startY = e.touches[0].clientY;
    });

    modal.addEventListener('touchmove', function (e) {
        const currentY = e.touches[0].clientY;
        const diffY = currentY - startY;

        if (diffY > 0) {
            modalContent.classList.add('translate-drag');
            modalContent.style.setProperty('--dragY', `${diffY}px`);
        }
    });

    modal.addEventListener('touchend', function (e) {
        const endY = e.changedTouches[0].clientY;
        const diffY = endY - startY;

        modalContent.classList.remove('translate-drag');

        if (diffY > 100) {
            closeModal();
        } else {
            modalContent.classList.add('translate-reset');
            modalContent.style.setProperty('--dragY', `0px`);
        }
    });

    function closeModal() {
        modalContent.classList.remove('translate-reset', 'translate-drag');
        modalContent.classList.add('translate-hide');

        setTimeout(() => {
            modal.classList.remove('show');
            document.body.classList.remove('modal-open');
            modalContent.classList.remove('translate-hide');
            modalContent.classList.add('translate-reset');
            modalContent.style.removeProperty('--dragY');
        }, 300);
    }
});
