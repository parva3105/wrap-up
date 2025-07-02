export interface PromptInput {
    prompt : string;
}

export interface CommandInput {
    command: string;
}

export interface CommandResponse {
    command : string;
}

export interface ExecutionResult {
    stdout: string;
    stderr?: string;
    error?: string;
}