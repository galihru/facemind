const installButton = document.getElementById('installButton');
      const modal = document.getElementById('swipeableModal');
      const cancelInstall = document.getElementById('cancelInstall');
      let startY;
      installButton.onclick = function() {
        modal.classList.add('show');
        document.body.classList.add('modal-open')
      };
      cancelInstall.onclick = function() {
        closeModal()
      };
      modal.addEventListener('touchstart', function(e) {
        startY = e.touches[0].clientY
      });
      modal.addEventListener('touchmove', function(e) {
        const currentY = e.touches[0].clientY;
        const diffY = currentY - startY;
        if (diffY > 0) {
          modal.querySelector('.modal-content').style.transform = `translateY(${diffY}px)`
        }
      });
      modal.addEventListener('touchend', function(e) {
        const endY = e.changedTouches[0].clientY;
        const diffY = endY - startY;
        if (diffY > 100) {
          closeModal()
        } else {
          modal.querySelector('.modal-content').style.transform = 'translateY(0)'
        }
      });

      function closeModal() {
        modal.querySelector('.modal-content').style.transform = 'translateY(100%)';
        setTimeout(() => {
          modal.classList.remove('show');
          document.body.classList.remove('modal-open');
          modal.querySelector('.modal-content').style.transform = 'translateY(0)'
        }, 300)
      }
