// Register service worker
if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('https://apps.ukmpenelitianunnes.com/sw.js').then(function(registration) {
                // Registration was successful
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            }, function(err) {
                // registration failed :(
                console.log('ServiceWorker registration failed: ', err);
            });
        });
    }

// Handle install prompt
let deferredInstallPrompt = null;
window.addEventListener('beforeinstallprompt', function (event) {
  event.preventDefault();
  deferredInstallPrompt = event;
  showInstallPrompt();
});

function showInstallPrompt() {
  // Lock body scroll
  document.body.style.overflow = 'hidden';

  // Create modal
  const modal = document.createElement('div');
  modal.style.position = 'fixed';
  modal.style.top = '0';
  modal.style.left = '0';
  modal.style.width = '100%';
  modal.style.height = '100%';
  modal.style.background = 'rgba(0, 0, 0, 0.5)';
  modal.style.display = 'flex';
  modal.style.justifyContent = 'center';
  modal.style.alignItems = 'center';
  modal.style.zIndex = '1000';
  modal.style.transition = 'transform 0.3s ease-out'; // Smooth transition

  // Create install prompt
  const installPrompt = document.createElement('div');
  installPrompt.style.padding = '20px';
  installPrompt.style.borderRadius = '30px';
  installPrompt.style.width = '80%';
  installPrompt.style.bottom = '70px';
  installPrompt.style.position = 'absolute';
  installPrompt.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.2)';
  installPrompt.style.transition = 'opacity 0.3s ease-out';
  installPrompt.innerHTML = `
  <style>
    /* Theme auto-adapt */
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

    /* Optional styling for better UI */
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
  </style>
  <div class="slide-top"></div>
  <img src="../192x192px.png" alt="logo" style="background: white; border-radius: 25px;">
  <h2>Face Mind</h2>
  <p>Application uses computer vision and machine learning to analyze mental health based on facial expressions</p>
  <button id="install-button">Install</button>
`;

  // Add event listener to install button
  installPrompt.querySelector('#install-button').addEventListener('click', function () {
    if (deferredInstallPrompt) {
      deferredInstallPrompt.prompt();
      deferredInstallPrompt.userChoice
        .then(function (choiceResult) {
          if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the install prompt');
          } else {
            console.log('User dismissed the install prompt');
          }
        });
    }
  });

  // Add swipe event listener to modal with dynamic translateY
  let swipeStartY = 0;
  let deltaY = 0;
  modal.addEventListener('touchstart', function (event) {
    swipeStartY = event.touches[0].clientY;
    console.log('touchstart: ', swipeStartY);
  });
  modal.addEventListener('touchmove', function (event) {
    let currentY = event.touches[0].clientY;
    deltaY = currentY - swipeStartY;
    console.log('touchmove: deltaY = ', deltaY);

    // Prevent modal from moving up
    if (deltaY > 0) {
        modal.style.transform = `translateY(${deltaY}px)`;
    }
  });
  modal.addEventListener('touchend', function () {
    console.log('touchend: deltaY = ', deltaY);
    if (deltaY > 100) { // Threshold untuk swipe
        // Animate modal sliding down and remove
        modal.style.transform = `translateY(100%)`;
        setTimeout(function () {
            modal.remove();
            // Unlock body scroll
            document.body.style.overflow = '';
            // Reload the page
        }, 300);
    } else {
        // If swipe is not enough, reset position
        modal.style.transform = 'translateY(0)';
    }
    // Reset deltaY
    deltaY = 0;
  });
  // Append modal and install prompt to body
  document.body.appendChild(modal);
  modal.appendChild(installPrompt);
}
