import React, { useContext, useEffect } from "react";
import { FiMoon, FiSun } from "react-icons/fi";
import { ThemeContext } from "../../contexts/theme";
import "./Theme.css";
interface Props {}

const updateTheme = (isDarkEnabled: boolean) => {
  // Get CSS variables for background/foreground
  const styles = getComputedStyle(document.body);
  const black = styles.getPropertyValue("--black");
  const white = styles.getPropertyValue("--white");
  const docEl = document.documentElement;

  if (isDarkEnabled) {
    docEl.style.setProperty("--background", black);
    docEl.style.setProperty("--foreground", white);
    const element = document.querySelector("html");
    if (element) {
      element.classList.add("darkmode");
    }
  } else {
    docEl.style.setProperty("--background", white);
    docEl.style.setProperty("--foreground", black);
    const element = document.querySelector("html");
    if (element) {
      element.classList.add("darkmode");
    }
  }
};

const ThemeSwitcher: React.FC<Props> = (): JSX.Element => {
  const { toggleTheme, themeName } = useContext(ThemeContext);
  const isEnabled = themeName === "light";
  useEffect(() => {
    updateTheme(isEnabled);
  }, [isEnabled]);

  return (
    <label className="toggle-wrapper" htmlFor="toggle">
      <div className={`toggle ${isEnabled ? "enabled" : "disabled"}`}>
        <span className="hidden">
          {isEnabled ? "Enable Light Mode" : "Enable Dark Mode"}
        </span>
        <div className="icons">
          <FiSun />
          <FiMoon />
        </div>
        <input
          id="toggle"
          name="toggle"
          type="checkbox"
          checked={isEnabled}
          onClick={toggleTheme}
        />
      </div>
    </label>
  );
};

export default ThemeSwitcher;
