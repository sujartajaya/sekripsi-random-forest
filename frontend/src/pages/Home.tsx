import { useEffect, useState } from "react";
import api from "../services/api";

import StatsCard from "../components/dashboard/StatsCard";
import StatusCard from "../components/dashboard/StatusCard";
import ModelInfo from "../components/dashboard/ModelInfo";

interface ModelInfoType {
  accuracy: number;
  precision: number;
  recall: number;
  dataset_rows: number;

  model_type?: string;
  n_trees?: number;
  max_depth?: number;
  min_samples_split?: number;
  min_samples_leaf?: number;
  max_features?: string;
  criterion?: string;
  random_state?: number;
}

export default function Home() {
  const [modelInfo, setModelInfo] = useState<ModelInfoType | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchModelInfo = async () => {
      try {
        const response = await api.get("/model/load-model");

        const data: ModelInfoType = response.data.model_info;
        console.log("Model Info:");
        console.log(data);
        setModelInfo(data);
      } catch (error) {
        console.error("Gagal mengambil model info:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchModelInfo();
  }, []);

  return (
    <div>
      <h1 className="text-5xl font-bold text-green-400">
        🌲 Random Forest Dashboard
      </h1>

      <p className="mt-3 text-gray-400 text-lg">
        Sistem Prediksi Machine Learning menggunakan algoritma Random Forest
      </p>

      <div className="grid grid-cols-4 gap-5 mt-10">
        <StatsCard
          title="Accuracy"
          value={
            loading || !modelInfo
              ? "Loading..."
              : `${(modelInfo.accuracy * 100).toFixed(2)}%`
          }
        />

        <StatsCard
          title="Precision"
          value={
            loading || !modelInfo
              ? "Loading..."
              : `${(modelInfo.precision * 100).toFixed(2)}%`
          }
        />

        <StatsCard
          title="Recall"
          value={
            loading || !modelInfo
              ? "Loading..."
              : `${(modelInfo.recall * 100).toFixed(2)}%`
          }
        />

        <StatsCard
          title="Dataset"
          value={
            loading || !modelInfo
              ? "Loading..."
              : `${modelInfo.dataset_rows} Rows`
          }
        />
      </div>

      <div className="grid grid-cols-2 gap-10 mt-10">
        <div>
          <h2 className="text-4xl font-bold mb-5">📌 Tentang Project</h2>

          <p className="text-gray-300 leading-8">
            Dashboard ini digunakan untuk melakukan prediksi data menggunakan
            algoritma Random Forest yang dibangun menggunakan Python dan
            FastAPI.
          </p>
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
