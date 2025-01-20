// Simple SHA-256 hash function for hashing the CSS content
function sha256(str) {
    const buffer = new TextEncoder("utf-8").encode(str);
    return window.crypto.subtle.digest("SHA-256", buffer).then(hashBuffer => {
        return Array.from(new Uint8Array(hashBuffer)).map(byte => byte.toString(16).padStart(2, '0')).join('');
    });
}

// Function to hash the CSS and dynamically apply it
async function hashAndApplyCSS() {
    const cssContent = `
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #1A1A3D;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
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
    `;

    // Hash the CSS content
    const cssHash = await sha256(cssContent);

    // Add the hash to the <style> tag's id or as a data attribute (to make it unique)
    const styleTag = document.createElement('style');
    styleTag.id = `css-${cssHash}`;
    styleTag.textContent = cssContent;
    document.head.appendChild(styleTag);
}

// Apply hashed CSS on page load
window.onload = function () {
    hashAndApplyCSS();
}
