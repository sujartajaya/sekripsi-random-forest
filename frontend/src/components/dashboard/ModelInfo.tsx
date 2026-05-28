export default function ModelInfo() {
  return (
    <div className="bg-[#111827] rounded-2xl p-5 mt-6">
      <h2 className="text-2xl font-bold mb-4">📊 Model Information</h2>

      <pre className="text-orange-400 overflow-auto">
        {`{
          "Model": "Random Forest",
          "Trees": 100,
          "Accuracy": "96%",
          "Dataset": 292
        }`}
      </pre>
    </div>
  );
}
