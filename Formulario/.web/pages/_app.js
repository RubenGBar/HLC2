/** @jsxImportSource @emotion/react */

import '$/styles/styles.css'

import { Fragment, StrictMode } from "react"
import RadixThemesColorModeProvider from "$/components/reflex/radix_themes_color_mode_provider.js"
import { Theme as RadixThemesTheme } from "@radix-ui/themes"
import theme from "$/utils/theme.js"


import { EventLoopProvider, StateProvider, defaultColorMode } from "$/utils/context.js";
import { ThemeProvider } from 'next-themes'
import * as next_link from "next/link";
import * as radix_ui_themes from "@radix-ui/themes";
import * as React from "react";
import * as emotion_react from "@emotion/react";
import * as utils_context from "$/utils/context";
import * as utils_state from "$/utils/state";


function AppWrap({children}) {
  




  return (
    <StrictMode>

<RadixThemesColorModeProvider>

<RadixThemesTheme accentColor={"blue"} css={{...theme.styles.global[':root'], ...theme.styles.global.body}}>

<Fragment>

{children}
</Fragment>
</RadixThemesTheme>
</RadixThemesColorModeProvider>
</StrictMode>
  )
}

export default function MyApp({ Component, pageProps }) {
  React.useEffect(() => {
    // Make contexts and state objects available globally for dynamic eval'd components
    let windowImports = {
      "next/link": next_link,
      "@radix-ui/themes": radix_ui_themes,
      "react": React,
      "@emotion/react": emotion_react,
      "$/utils/context": utils_context,
      "$/utils/state": utils_state,
    };
    window["__reflex"] = windowImports;
  }, []);
  return (
    <ThemeProvider defaultTheme={ defaultColorMode } attribute="class">
      <StateProvider>
        <EventLoopProvider>
            <AppWrap>
              <Component {...pageProps} />
            </AppWrap>
        </EventLoopProvider>
      </StateProvider>
    </ThemeProvider>
  );
}

