require "rake/clean"
require "shellwords"

COPYRIGHT_JS = "_includes/copyright.js"
JS_SOURCES = [
  "assets/js/vendor/jquery/jquery-3.6.0.js",
  *Dir.glob("assets/js/plugins/*.js").sort,
  "assets/js/_main.js"
]
JS_TARGET = "assets/js/main.min.js"

task default: :js

file COPYRIGHT_JS do |t|
  File.write(
    t.name,
    <<~HEADER
      /*!
       * Minimal Mistakes Jekyll Theme assets
       * Original theme copyright: Michael Rose, MIT License
       * Customized for MouseBall54's Toolbox
       */
    HEADER
  )
end

task js: JS_TARGET

file JS_TARGET => [COPYRIGHT_JS, *JS_SOURCES] do |t|
  sh Shellwords.join([
    "npx", "uglifyjs",
    "-c",
    "--comments", "/Minimal Mistakes|MouseBall54/",
    "--source-map",
    "-m",
    "-o", t.name,
    *t.prerequisites
  ])
end

CLEAN.include(JS_TARGET)
