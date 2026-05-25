export interface Question {
  field: string;
  question: string;
  type: string;
  choices?: string[];
}

export interface QuestionResponse {
  total: number;
  questions: Question[];
}
