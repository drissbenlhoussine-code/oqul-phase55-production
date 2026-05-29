import { create } from "zustand";

type AppStore = {
  activeChildId: string | null;
  sidebarOpen: boolean;
  setActiveChildId: (childId: string | null) => void;
  setSidebarOpen: (open: boolean) => void;
};

export const useAppStore = create<AppStore>((set) => ({
  activeChildId: null,
  sidebarOpen: false,
  setActiveChildId: (activeChildId) => set({ activeChildId }),
  setSidebarOpen: (sidebarOpen) => set({ sidebarOpen }),
}));
