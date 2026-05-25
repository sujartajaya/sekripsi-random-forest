import { useState } from "react";

import Sidebar from "./Sidebar";

import { Menu } from "lucide-react";

interface Props {
  children: React.ReactNode;
}

export default function MainLayout({ children }: Props) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#050816] text-white flex">
      {/* SIDEBAR */}
      <Sidebar isOpen={isOpen} setIsOpen={setIsOpen} />

      {/* CONTENT */}
      <div className="flex-1 flex flex-col">
        {/* MOBILE NAVBAR */}
        <header
          className="
            lg:hidden
            flex items-center
            p-4
            border-b border-gray-800
          "
        >
          <button onClick={() => setIsOpen(true)}>
            <Menu />
          </button>

          <h1 className="ml-4 font-bold">RF Dashboard</h1>
        </header>

        {/* PAGE */}
        <main className="flex-1 p-4 lg:p-10 overflow-auto">{children}</main>
      </div>
    </div>
  );
}
