const https = require('https');
const fs = require('fs');

const file = fs.createWriteStream("images.zip");
https.get("https://real-esate-oghre.ondigitalocean.app/download-images", function(response) {
  response.pipe(file);
  file.on("finish", () => {
    file.close();
    console.log("Download complete!");
  });
});
