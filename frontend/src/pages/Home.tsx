import StatsCard from "../components/dashboard/StatsCard";
import StatusCard from "../components/dashboard/StatusCard";
import ModelInfo from "../components/dashboard/ModelInfo";

export default function Home() {
  return (
    <div>
      <h1 className="text-5xl font-bold text-green-400">
        🌲 Random Forest Dashboard
      </h1>

      <p className="mt-3 text-gray-400 text-lg">
        Sistem Prediksi Machine Learning menggunakan algoritma Random Forest
      </p>

      <div className="grid grid-cols-4 gap-5 mt-10">
        <StatsCard title="Accuracy" value="96%" />
        <StatsCard title="Precision" value="94%" />
        <StatsCard title="Recall" value="95%" />
        <StatsCard title="Dataset" value="292 Rows" />
      </div>

      <div className="grid grid-cols-2 gap-10 mt-10">
        <div>
          <h2 className="text-4xl font-bold mb-5">📌 Tentang Project</h2>

          <p className="text-gray-300 leading-8">
            Dashboard ini digunakan untuk melakukan prediksi data menggunakan
            algoritma Random Forest yang dibangun menggunakan Python dan
            FastAPI.
          </p>

          <ul className="mt-6 space-y-3 list-disc ml-5 text-gray-300">
            <li>Prediksi realtime</li>
            <li>Analisis model</li>
            <li>Visualisasi data</li>
            <li>History prediksi</li>
            <li>Monitoring machine learning</li>
          </ul>
        </div>

        <div>
          <h2 className="text-4xl font-bold mb-5">⚡ Status System</h2>

          <div className="space-y-4">
            <StatusCard title="FastAPI Connected" />
            <StatusCard title="Model Loaded" />
            <StatusCard title="React Running" />
          </div>

          <ModelInfo />
        </div>
      </div>
    </div>
  );
}
