if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('https://apps.ukmpenelitianunnes.com/sw.js').then(function(registration) {
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}

let deferredInstallPrompt = null;

window.addEventListener('beforeinstallprompt', function(event) {
  event.preventDefault();
  deferredInstallPrompt = event;
  showInstallPrompt();
});

function showInstallPrompt() {
  document.body.style.overflow = 'hidden';

  // Create the modal container
  const modal = document.createElement('div');
  modal.style.position = 'fixed';
  modal.style.top = '0';
  modal.style.left = '0';
  modal.style.width = '100%';
  modal.style.height = '100%';
  modal.style.background = 'rgba(0,0,0,0.5)';
  modal.style.display = 'flex';
  modal.style.justifyContent = 'center';
  modal.style.alignItems = 'center';
  modal.style.zIndex = '1000';
  modal.style.transition = 'transform 0.3s ease-out';

  // Create the install prompt box
  const installPrompt = document.createElement('div');
  installPrompt.style.padding = '20px';
  installPrompt.style.borderRadius = '30px';
  installPrompt.style.width = '80%';
  installPrompt.style.bottom = '70px';
  installPrompt.style.position = 'absolute';
  installPrompt.style.boxShadow = '0 0 10px rgba(0,0,0,0.2)';
  installPrompt.style.transition = 'opacity 0.3s ease-out';

  // Create the style tag and add styles
  const style = document.createElement('style');
  style.innerHTML = `
    @media (prefers-color-scheme: dark) {
      div {
        background-color: #1a202c;
        color: #fff;
      }
    }

    @media (prefers-color-scheme: light) {
      div {
        background: radial-gradient(100% 193.51% at 100% 0%, #EDF4F8 0%, #EFF2FA 16.92%, #FAEFF6 34.8%, #FAE6F2 48.8%, #FAF0F7 63.79%, #F1F1FB 81.34%, #F0F4F8 100%);
        color: #000;
      }
    }

    h2 {
      margin-bottom: 10px;
      font-size: 1.5em;
    }

    p {
      font-size: 1em;
      margin-bottom: 20px;
    }

    button {
      padding: 10px 20px;
      border: none;
      border-radius: 50px;
      background-color: #0050A8;
      color: white;
      cursor: pointer;
      width: 100%;
    }

    button:hover {
      background-color: #0056b3;
    }

    .slide-top {
      width: 50px;
      height: 5px;
      background-color: white;
      border-radius: 5px;
      position: absolute;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
    }

    img {
      position: relative;
      left: 50%;
      transform: translate(-50%, 10px);
      background-size: cover;
      width: 85px;
      margin: 0;
      padding: 0;
    }
  `;
  document.head.appendChild(style);  // Append styles to the head

  // Add the inner HTML to the install prompt
  installPrompt.innerHTML = `
    <div class="slide-top"></div>
    <img src="./192x192px.png" alt="logo" style="background: white; border-radius: 25px;">
    <h2>Face Mind</h2>
    <p>Application uses computer vision and machine learning to analyze mental health based on facial expressions</p>
    <button id="install-button">Install</button>
  `;

  // Add event listener to the install button
  installPrompt.querySelector('#install-button').addEventListener('click', function() {
    if (deferredInstallPrompt) {
      deferredInstallPrompt.prompt();
      deferredInstallPrompt.userChoice.then(function(choiceResult) {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the install prompt');
        } else {
          console.log('User dismissed the install prompt');
        }
      });
    }
  });

  // Handling swipe events for closing the modal
  let swipeStartY = 0;
  let deltaY = 0;

  modal.addEventListener('touchstart', function(event) {
    swipeStartY = event.touches[0].clientY;
  });

  modal.addEventListener('touchmove', function(event) {
    let currentY = event.touches[0].clientY;
    deltaY = currentY - swipeStartY;
    if (deltaY > 0) {
      modal.style.transform = `translateY(${deltaY}px)`;
    }
  });

  modal.addEventListener('touchend', function() {
    if (deltaY > 100) {
      modal.style.transform = `translateY(100%)`;
      setTimeout(function() {
        modal.remove();
        document.body.style.overflow = '';
      }, 300);
    } else {
      modal.style.transform = 'translateY(0)';
    }
    deltaY = 0;
  });

  // Append the modal and install prompt to the body
  document.body.appendChild(modal);
  modal.appendChild(installPrompt);
}
