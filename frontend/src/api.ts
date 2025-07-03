import axios from 'axios';
import type { PromptInput, CommandInput, ExecutionResult } from './types';

const BASE_URL = 'http://localhost:8000'; // Adjust this if deploying

// Sends user prompt → gets command from LLM
export async function generateCommand(data: PromptInput): Promise<{ command: string }> {
  const response = await axios.post(`${BASE_URL}/generate-command`, data);
  return response.data;
}

// Sends command → executes it if safe
export async function executeCommand(data: CommandInput): Promise<ExecutionResult> {
  const response = await axios.post(`${BASE_URL}/execute`, data);
  return response.data;
}
