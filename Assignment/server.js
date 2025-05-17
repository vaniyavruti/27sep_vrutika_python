const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { exec } = require('child_process');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post('/run', (req, res) => {
  const code = req.body.code;
  
  exec(`echo "${code}" | node`, (error, stdout, stderr) => {
    if (error) {
      res.send({ output: stderr || error.message });
    } else {
      res.send({ output: stdout });
    }
  });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
