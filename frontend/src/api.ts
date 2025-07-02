import axios from 'axios';
import { PromptInput, CommandInput, CommandResponse, ExecutionResult } from './types';


const API_BASE = "https://127.0.0.1:8000" //backend URL

export const generateCommand = async(data: PromptInput): Promise<CommandResponse> => {
    const response = await axios.post(`${API_BASE}/generate-command`, data);
    return response.data;
}

export const executeCommand = async(data: CommandInput): Promise<ExecutionResult> => {
    const response = await axios.post(`${API_BASE}/execute`, data);
    return response.data
}