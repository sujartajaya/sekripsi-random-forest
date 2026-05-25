import { useEffect, useState } from "react";
import api from "../services/api";

import type { Question, QuestionResponse } from "../types/question";

export default function Prediction() {
  const [questions, setQuestions] = useState<Question[]>([]);

  const [loading, setLoading] = useState(true);

  const [formData, setFormData] = useState<Record<string, any>>({});

  const [result, setResult] = useState<any>(null);

  const [submitLoading, setSubmitLoading] = useState(false);

  // =========================
  // GET QUESTIONS
  // =========================
  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await api.get<QuestionResponse>("/questions/");
        console.log(response.data);
        setQuestions(response.data.questions);
      } catch (error) {
        console.error("Failed get questions", error);
      } finally {
        setLoading(false);
      }
    };

    fetchQuestions();
  }, []);

  // =========================
  // HANDLE INPUT
  // =========================
  const handleChange = (field: string, value: any) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  // =========================
  // SUBMIT
  // =========================
  const handleSubmit = async () => {
    try {
      setSubmitLoading(true);
      setResult(null);
      const response = await api.post("/model/predict", formData);
      console.log("Prediction Result:");
      console.log(response.data);
      setResult(response.data);
    } catch (error) {
      console.error("Prediction failed:", error);
    } finally {
      setSubmitLoading(false);
    }
  };

  return (
    <div>
      {/* HEADER */}
      <h1 className="text-5xl font-bold mb-10">🔮 Prediction Page</h1>

      {/* CARD */}
      <div className="bg-[#111827] p-10 rounded-2xl">
        {loading ? (
          <p>Loading questions...</p>
        ) : (
          <div className="space-y-8">
            {questions.map((item, index) => (
              <div key={item.field}>
                {/* QUESTION */}
                <label className="block mb-3 text-lg font-semibold">
                  {index + 1}. {item.question}
                </label>

                {/* BINARY */}
                {item.type === "binary" && (
                  <div className="flex gap-5">
                    <button
                      type="button"
                      onClick={() => handleChange(item.field, 1)}
                      className={`px-5 py-2 rounded-xl transition
                      ${
                        formData[item.field] === 1
                          ? "bg-green-600"
                          : "bg-gray-700 hover:bg-gray-600"
                      }`}
                    >
                      Yes
                    </button>

                    <button
                      type="button"
                      onClick={() => handleChange(item.field, 0)}
                      className={`px-5 py-2 rounded-xl transition
                      ${
                        formData[item.field] === 0
                          ? "bg-red-600"
                          : "bg-gray-700 hover:bg-gray-600"
                      }`}
                    >
                      No
                    </button>
                  </div>
                )}

                {/* INTEGER */}
                {item.type === "integer" && (
                  <input
                    type="number"
                    className="w-full bg-gray-800 border border-gray-700 rounded-xl px-4 py-3 outline-none"
                    onChange={(e) =>
                      handleChange(item.field, Number(e.target.value))
                    }
                  />
                )}

                {/* CATEGORICAL */}
                {item.type === "categorical" && (
                  <select
                    className="w-full bg-gray-800 border border-gray-700 rounded-xl px-4 py-3 outline-none"
                    onChange={(e) => handleChange(item.field, e.target.value)}
                  >
                    <option value="">Select option</option>

                    {item.choices?.map((choice) => (
                      <option key={choice} value={choice}>
                        {choice}
                      </option>
                    ))}
                  </select>
                )}
              </div>
            ))}

            {/* BUTTON */}
            <button
              onClick={handleSubmit}
              disabled={submitLoading}
              className="mt-10 bg-blue-600 hover:bg-blue-700 transition px-8 py-4 rounded-2xl font-bold text-lg disabled:bg-gray-600"
            >
              {submitLoading ? "Predicting..." : "Predict Now"}
            </button>
            {/* RESULT */}
            {result && (
              <div className="mt-10 bg-[#0F172A] border border-green-700 rounded-2xl p-8">
                <h2 className="text-3xl font-bold mb-8 text-green-400">
                  Prediction Result
                </h2>

                {/* LABEL */}
                <div className="mb-8">
                  <div
                    className={`text-4xl font-bold ${
                      result.prediction.prediction === 1
                        ? "text-red-400"
                        : "text-green-400"
                    }`}
                  >
                    {result.prediction.label}
                  </div>
                </div>

                {/* DETAIL */}
                <div className="space-y-5 text-lg">
                  {/* PREDICTION */}
                  <div className="flex justify-between border-b border-gray-700 pb-3">
                    <span className="text-gray-400">Prediction Value</span>

                    <span className="font-bold">
                      {result.prediction.prediction}
                    </span>
                  </div>

                  {/* ASD */}
                  <div className="flex justify-between border-b border-gray-700 pb-3">
                    <span className="text-gray-400">ASD Probability</span>

                    <span className="font-bold text-red-400">
                      {result.prediction.probability.asd}%
                    </span>
                  </div>

                  {/* NO ASD */}
                  <div className="flex justify-between border-b border-gray-700 pb-3">
                    <span className="text-gray-400">No ASD Probability</span>

                    <span className="font-bold text-green-400">
                      {result.prediction.probability.no_asd}%
                    </span>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
