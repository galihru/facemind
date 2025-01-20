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

  const jsFiles = ['st.js', 'dfs.js'];

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
    `;
   // Menambahkan file JavaScript dengan atribut integrity dan crossorigin
  jsFiles.forEach(file => {
    const filePath = path.join(process.cwd(), file);
    const integrityHash = generateIntegrityHash(filePath);
    htmlContent += `
        <script src="${file}" nonce="${nonce}" integrity="sha384-${integrityHash}" crossorigin="anonymous"></script>
    `;
  });
  htmlContent += `
    <style nonce="${nonce}">
        body {
          margin: 0;
          overflow: hidden;
        }
        .container {
            text-align: center;
            max-width: 400px;
        }

        .header-image {
            margin-top: 20px;
        }

        .header-image img {
            width: 100%;
            height: auto;
        }

        .content {
            background-color: #2C2C54;
            padding: 20px;
            border-radius: 20px;
            margin-top: 20px;
        }

        .content h2 {
            margin: 10px 0;
            font-size: 24px;
        }

        .content p {
            font-size: 16px;
            margin: 10px 0;
        }

        button {
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        button {
            padding: 15px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            align-items: center;
        }

        button .start-checkin {
            background-color: #4A4AFF;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        button .start-checkin:hover {
            background-color: #3C3CFF;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }

        button .start-checkin:active {
            background-color: #2C2CFF;
            transform: translateY(1px);
        }

        button .later {
            background-color: #E0E0E0;
            color: #4A4AFF;
            border: 2px solid #4A4AFF;
            font-weight: bold;
        }

        button .later:hover {
            background-color: #D0D0D0;
            transform: translateY(-2px);
        }

        button .later:active {
            background-color: #B0B0B0;
            transform: translateY(1px);
        }

        .note {
            font-size: 12px;
            color: #B0B0B0;
            margin-top: 10px;
        }

        /* Modal Styles */
        .modal {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: auto;
            display: none;
            justify-content: center;
            align-items: flex-end;
            background: rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
        }

        .modal.show {
            display: flex;
            transform: translateY(0);
        }

        .modal-content {
            background: #2c2c54;
            width: 100%;
            padding: 20px;
            border-radius: 20px 20px 0 0;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            position: relative;
            transition: transform 0.3s ease;
        }

        .modal h2 {
            font-size: 20px;
            margin: 10px 0;
        }

        .modal button {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
        }

        .modal button#confirmInstall {
            background-color: #4A4AFF;
            color: white;
            margin-bottom: 10px;
        }

        .modal button#cancelInstall {
            background-color: #E0E0E0;
            color: #4A4AFF;
        }

        /* Swipe indicator */
        .swipe-indicator {
            width: 50px;
            height: 5px;
            background-color: white;
            border-radius: 5px;
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
        }

        /* Lock scroll on body when modal is open */
        body.modal-open {
            overflow: hidden;
        }
    </style>
    </head>
    <body>
        <div class="container">
        <div class="header-image">
            <img alt="Illustration of a head with a plant growing from it, symbolizing growth and reflection"
                src="./layarui.png" />
        </div>
        <div class="content">
            <h2>Face Mind</h2>
            <h3>Face the Future of Mental Health</h3>
            <p>Solution Application based on Computer Vision, and Integrated with Instagram Apps</p>
            <button type="button" class="start-checkin" id="installButton">Install Application</button>
            <button type="button" class="later">Later</button>
        </div>
        <p class="note">Note that you won't be able to proceed to the next touch session unless you complete the
            check-in</p>
    </div>

    <!-- Modal -->
    <div class="modal" id="swipeableModal">
        <div class="modal-content">
            <!-- Swipeable indicator -->
            <div class="swipe-indicator"></div>
            <img alt="Illustration of a head with a plant growing from it, symbolizing growth and reflection"
                src="./logofm.png" style="width: inherit; background: white; border-radius: 15px;" />
            <h2>Install Application</h2>
            <button type="button" id="confirmInstall">Yes, Install</button>
            <button type="button" id="cancelInstall">Cancel</button>
        </div>
    </div>
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
