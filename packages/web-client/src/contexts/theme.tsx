import { createContext, useEffect, useState } from "react";

type ThemeItem = "light" | "dark";
type ThemeContextType = {
  themeName: ThemeItem;
  toggleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextType>({
  themeName: "dark",
  toggleTheme: () => {},
});

const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [themeName, setThemeName] = useState<ThemeItem>(
    (localStorage.getItem("ui.theme") as "light" | "dark") || "dark"
  );

  useEffect(() => {
    const darkMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    setThemeName(darkMediaQuery.matches ? "dark" : "light");
    darkMediaQuery.addEventListener("change", (e) => {
      setThemeName(e.matches ? "dark" : "light");
    });
  }, []);

  const toggleTheme = () => {
    const name = themeName === "dark" ? "light" : "dark";
    localStorage.setItem("themeName", name);
    setThemeName(name);
  };

  return (
    <ThemeContext.Provider value={{ themeName, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export { ThemeContext, ThemeProvider };
