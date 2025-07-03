import { useState } from 'react'
import './App.css'
import { generateCommand, executeCommand } from './Api'
import type { PromptInput, CommandInput, ExecutionResult } from './types'


function App() {
    const[prompt, setPrompt] = useState("")
    const[suggestedCommand, setSuggestedCommand] = useState<string | null>(null);
    const[executionResult, setExecutionResult] = useState<ExecutionResult| null>(null);
    const[error, setError] = useState<string | null>(null);


    // generates the command from prompt
    const handleGenerate = async () => {  
      try{
        setExecutionResult(null);
        setError(null);
        const response = await generateCommand({prompt} as PromptInput);
        setSuggestedCommand(response.command);
      } catch (err: unknown) {
          if (err instanceof Error) {
            setError(err.message);
          } else {
            setError("Failed to generate command")
          }
      }
    };

    const handleExecute = async () => {
      try {
        if (!suggestedCommand) return;
        const response = await executeCommand({ command: suggestedCommand } as CommandInput);
        
        console.log("Backend Response:", response); 

        setExecutionResult(response); 

        if (response.stderr) {
          setError(response.stderr);  
        } else {
          setError(null);
        }
      } catch (err: unknown) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("An unexpected error occurred.");
        }
      }
    };

    return (
      <div className="container">
        <h1>WindowWrap</h1>
        <input 
          type="text"
          placeholder="What do you wanna do ?"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)} 
        />
        <button onClick={handleGenerate}>Generate Command</button>

        {suggestedCommand && (
          <div className="suggestion">
            <p><strong>Suggested Command:</strong> <code>{suggestedCommand}</code></p>
            <button onClick={handleExecute}>Run Command</button>
          </div>
        )}

        {executionResult && (
          <div>
            <strong>STDOUT: </strong>
            <pre>{executionResult.stdout}</pre>

            {executionResult.stderr && executionResult.stderr.trim() !== "" && (
              <>
                <strong>STDERR: </strong>
                <pre>{executionResult.stderr}</pre>
              </>
            )}
          </div>
        )}

        {error && (
          <div className="error">
            <strong>Error: </strong> {error}
          </div>
        )}

      </div>
    );
  }

export default App;
