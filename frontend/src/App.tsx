import { useState } from 'react'
import './App.css'
import { generateCommand, executeCommand } from './api'
import { PromptInput, CommandInput, ExecutionResult } from './types'


function App() {
    const[prompt, setPrompt] = useState("")
    const[suggestedCommand, setSuggestedCommand] = useState<string | null>(null);
    const[executionResult, setExecutionResult] = useState<ExecutionResult| null>(null);
    const[erros, setError] = useState<string | null>(null);


    // generates the command from prompt
    const handleGenerate = async () => {  
      try{
        setExecutionResult(null);
        setError(null);
        const response = await generateCommand({prompt} as PromptInput);
        setSuggestedCommand(response.command);
      } catch (err) {
        setError("Failed to generate command")
      }
    };
}

export default App
