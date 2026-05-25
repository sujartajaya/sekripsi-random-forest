interface Props {
  title: string;
}

export default function StatusCard({ title }: Props) {
  return (
    <div className="bg-green-900/40 border border-green-700 p-5 rounded-xl">
      ✅ {title}
    </div>
  );
}
