import Link from "next/link";

interface FeatureCardProps {
  title: string;
  description: string;
  icon: string;
  href: string;
}

export default function FeatureCard({ title, description, icon, href }: FeatureCardProps) {
  return (
    <Link href={href}>
      <div className="p-6 rounded-lg bg-gray-900/50 border border-gray-800 hover:border-gray-700 transition hover:bg-gray-900 hover:shadow-lg cursor-pointer h-full">
        <div className="text-4xl mb-4">{icon}</div>
        <h3 className="text-xl font-semibold mb-2 text-white">{title}</h3>
        <p className="text-gray-400 text-sm leading-relaxed">{description}</p>
      </div>
    </Link>
  );
}
