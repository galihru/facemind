import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { minify } from 'html-minifier';

// Fungsi untuk generate nonce sederhana
function generateNonce() {
  return Math.random().toString(36).substring(2, 15) + 
         Math.random().toString(36).substring(2, 15);
}

// Fungsi untuk menghitung hash file untuk SRI
// Fungsi untuk menghitung hash file untuk SRI
function generateIntegrityHash(filePath) {
  const fileBuffer = fs.readFileSync(filePath);
  const hash = crypto.createHash('sha384');
  hash.update(fileBuffer);
  return hash.digest('base64');
}

// Fungsi untuk mendapatkan waktu sekarang
function getCurrentTime() {
  const now = new Date();
  return now.toLocaleString(); // Format waktu sesuai dengan lokal
}

async function generateHtml() {
  // Generate nonce untuk setiap elemen
  const nonce = generateNonce();

  // Path untuk file JavaScript
  const jsFiles = ['inst.js', 'dfs.js'];

  // CSP yang diperbaiki dengan strict-dynamic
  const cspContent = [
    `style-src 'self' 'nonce-${nonce}' https://4211421036.github.io`,
    "object-src 'none'",
    "base-uri 'self'",
    "img-src 'self' data: https://4211421036.github.io",
    "default-src 'self' https://4211421036.github.io",
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic' 'unsafe-inline' 'sha384-${generateIntegrityHash(path.join(process.cwd(), jsFiles[0]))}' https://4211421036.github.io`,
    "font-src 'self' https://4211421036.github.io",
    "media-src 'self' https://4211421036.github.io",
    "connect-src 'self' https://4211421036.github.io",
    "form-action 'self'",
    "manifest-src 'self' https://4211421036.github.io",
    "worker-src 'self' blob: https://4211421036.github.io"
  ].join('; ');


  let htmlContent = `<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Facemind</title>
      <meta content="width=device-width,initial-scale=1" name=viewport>
      <meta content="Application uses computer vision and machine learning to analyze mental health based on facial expressions. The app includes login system, and real-time mental health analysis through facial landmarks, using OpenCV, Mediapipe, and PyQt5. This Application Delegation Paper Competition for" name=description>
      <meta content="GALIH RIDHO UTOMO; Ana Maulida" name=author>
      <link href=./logo.ico rel=icon type=image/x-icon>
      <link href=./manifest.json rel=manifest crossorigin=use-credentials>
      <meta charset=UTF-8>
      <meta name="robots" content="index, follow">
      <meta property="og:title" content="Facemind!">
      <meta property="og:description" content="Application uses computer vision and machine learning to analyze mental health based on facial expressions. The app includes login system, and real-time mental health analysis through facial landmarks, using OpenCV, Mediapipe, and PyQt5. This Application Delegation Paper Competition for">
      <meta property="og:type" content="website">
      <meta property="og:url" content="https://4211421036.github.io/facemind">
      <meta property="og:image" content="https://4211421036.github.io/facemind/192x192px.png">
      <meta name="twitter:card" content="summary_large_image">
      <meta name="twitter:title" content="Selamat Ulang Tahun!">
      <meta name="twitter:description" content="Selamat Ulang Tahun!">
      <meta property="og:locale" content="id" />
      <meta name="twitter:image" content="https://4211421036.github.io/facemind/192x192px.png">
      <meta property="og:image:alt" content="Facemind" />
      <meta property="og:type" content="website" />
      <meta property="og:audio:type" content="audio/mpeg" />
      <meta http-equiv="Content-Security-Policy" content="${cspContent}">
    </head>
    <body>
      <div class=container>
        <div class=header-image><img alt="Illustration of a head with a plant growing from it, symbolizing growth and reflection" src=./layarui.png></div>
        <div class=content>
          <h2>Face Mind</h2>
          <h3>Face the Future of Mental Health</h3>
          <p>Solution Application based on Computer Vision, and Integrated with Instagram Apps</p><button type=button id=installButton class=start-checkin>Install Application</button><button type=button class=later onclick=closeTab()>Later</button>
        </div>
        <p class=note>Note that you won't be able to proceed to the next touch session unless you complete the check-in
      </div>
      <div class=modal id=swipeableModal>
        <div class=modal-content>
          <div class=swipe-indicator></div><img alt="Illustration of a head with a plant growing from it, symbolizing growth and reflection" src=./logofm.png>
          <h2>Install Application</h2><button type=button id=confirmInstall><a download=facemind.exe href=https://github.com/4211421036/facemind/releases/download/v1.1/facemind.exe style=text-decoration:none;color:#fff;width:100%;padding:15px;border:none;border-radius:25px;font-size:16px;cursor:pointer>Yes, Install</a></button><button type=button id=cancelInstall>Cancel</button>
        </div>
      </div>
      <script>
      function closeTab() {
        window.close()
      }
    </script>
    <style nonce="${nonce}">
        img {
          width: inherit;
          background: #fff;
          border-radius: 15px;
        }
    </style>
    <script nonce="${nonce}" src=""></script>
    <script nonce="${nonce}" src=""></script>
    <!-- page generated automatic: ${getCurrentTime()} -->
    </body>
  </html>`;

  try {
    // Minify HTML yang dihasilkan
    const minifiedHtml = await minify(htmlContent, {
      collapseWhitespace: true,  // Menghapus spasi dan baris kosong
      removeComments: true,      // Menghapus komentar
      removeRedundantAttributes: true, // Menghapus atribut yang tidak perlu
      useShortDoctype: true,     // Menggunakan doctype singkat
      minifyJS: true,            // Minify JS
      minifyCSS: true            // Minify CSS
    });

    // Tentukan path untuk file HTML yang akan dihasilkan
    const outputPath = path.join(process.cwd(), 'index.html');

    // Simpan HTML yang telah di-minify ke file
    fs.writeFileSync(outputPath, minifiedHtml);
    console.log('File HTML telah dibuat dan di-minify di:', outputPath);
  } catch (error) {
    console.error('Error during minification:', error);
  }
}

// Generate HTML
generateHtml();
