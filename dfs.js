const installButton = document.getElementById('installButton');
        const modal = document.getElementById('swipeableModal');
        const cancelInstall = document.getElementById('cancelInstall');
        let startY;

        // Open the modal when the "Install Application" button is clicked
        installButton.onclick = function () {
            modal.classList.add('show');
            document.body.classList.add('modal-open'); // Lock scroll
        }

        // Close the modal when the "Cancel" button is clicked
        cancelInstall.onclick = function () {
            closeModal();
        }

        // Swipe to close functionality
        modal.addEventListener('touchstart', function (e) {
            startY = e.touches[0].clientY;
        });

        modal.addEventListener('touchmove', function (e) {
            const currentY = e.touches[0].clientY;
            const diffY = currentY - startY;
            // Move modal while swiping
            if (diffY > 0) {
                modal.querySelector('.modal-content').style.transform = `translateY(${diffY}px)`;
            }
        });

        modal.addEventListener('touchend', function (e) {
            const endY = e.changedTouches[0].clientY;
            const diffY = endY - startY;

            // If the swipe is long enough (e.g. more than 100px), close the modal
            if (diffY > 100) {
                closeModal();
            } else {
                // Otherwise, reset the position of the modal
                modal.querySelector('.modal-content').style.transform = 'translateY(0)';
            }
        });

        function closeModal() {
            // Animate modal closing by translating it down
            modal.querySelector('.modal-content').style.transform = 'translateY(100%)';
            setTimeout(() => {
                modal.classList.remove('show');
                document.body.classList.remove('modal-open'); // Unlock scroll
                // Reset transform after modal is fully hidden
                modal.querySelector('.modal-content').style.transform = 'translateY(0)';
            }, 300); // Match the transition duration
        }
