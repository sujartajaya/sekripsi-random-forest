import { Link, useLocation } from "react-router-dom";
import { Home, Brain, X } from "lucide-react";

interface Props {
  isOpen: boolean;
  setIsOpen: (value: boolean) => void;
}

export default function Sidebar({ isOpen, setIsOpen }: Props) {
  const location = useLocation();

  const menus = [
    {
      name: "Home",
      path: "/",
      icon: <Home size={18} />,
    },
    {
      name: "Prediction",
      path: "/prediction",
      icon: <Brain size={18} />,
    },
  ];

  return (
    <>
      {/* OVERLAY MOBILE */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* SIDEBAR */}
      <aside
        className={`
          fixed lg:sticky
          top-0 left-0 z-50

          min-h-screen
          w-64

          bg-[#1B1F2E]
          p-5

          transform transition-transform duration-300

          ${isOpen ? "translate-x-0" : "-translate-x-full"}

          lg:translate-x-0
        `}
      >
        {/* HEADER */}
        <div className="flex items-center justify-between mb-10">
          <h1 className="text-xl font-bold text-white">🌲 RF Dashboard</h1>

          {/* CLOSE MOBILE */}
          <button
            className="lg:hidden text-white"
            onClick={() => setIsOpen(false)}
          >
            <X />
          </button>
        </div>

        {/* MENU */}
        <div className="space-y-2">
          {menus.map((menu) => (
            <Link
              key={menu.path}
              to={menu.path}
              onClick={() => setIsOpen(false)}
              className={`
                flex items-center gap-3
                px-4 py-3 rounded-xl
                transition text-white

                ${
                  location.pathname === menu.path
                    ? "bg-gray-700"
                    : "hover:bg-gray-800"
                }
              `}
            >
              {menu.icon}

              {menu.name}
            </Link>
          ))}
        </div>
      </aside>
    </>
  );
}
