interface Props {
  title: string;
  value: string;
}

export default function StatsCard({ title, value }: Props) {
  return (
    <div className="bg-[#111827] p-6 rounded-2xl shadow-lg">
      <p className="text-gray-400 text-sm">{title}</p>

      <h2 className="text-4xl font-bold mt-3">{value}</h2>
    </div>
  );
}
