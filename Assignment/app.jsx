import React, { useState } from 'react';
import axios from 'axios';
import { Controlled as CodeMirror } from '@uiw/react-codemirror';
import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/material.css';
import 'codemirror/mode/javascript/javascript';

function App() {
  const [code, setCode] = useState('// Write your JS code here');
  const [output, setOutput] = useState('');

  const runCode = async () => {
    try {
      const res = await axios.post('http://localhost:5000/run', { code });
      setOutput(res.data.output);
    } catch (err) {
      setOutput('Error running code.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Code Editor with Terminal</h2>
      <CodeMirror
        value={code}
        options={{
          mode: 'javascript',
          theme: 'material',
          lineNumbers: true,
        }}
        onBeforeChange={(editor, data, value) => setCode(value)}
      />
      <button onClick={runCode} style={{ marginTop: '10px' }}>
        Run Code
      </button>
      <pre style={{ background: '#111', color: '#0f0', padding: '10px', marginTop: '20px' }}>
        {output}
      </pre>
    </div>
  );
}

export default App;
