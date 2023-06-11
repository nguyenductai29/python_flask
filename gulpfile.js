const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const css = require("gulp-css");
const uglify = require("gulp-uglify");
const cssbeautify = require('gulp-cssbeautify');

gulp.task("css", function () {
    return gulp
        .src("static/css/*.css")
        .pipe(css())
        .pipe(cssbeautify())
        .pipe(gulp.dest("static/css"))
        .pipe(browserSync.stream());
});

gulp.task("js", function () {
    return gulp
        .src("static/js/*.js")
        .pipe(uglify())
        .pipe(gulp.dest("static/js"))
        .pipe(browserSync.stream());
});

gulp.task(
    "browser-sync",
    gulp.series("css", "js", function () {
        browserSync.init({
            proxy: "localhost:5000",
            notify: false,
            open: false,
        });

        gulp.watch("templates/**/*.html").on("change", browserSync.reload);
        gulp.watch("static/css/*.css", gulp.series("css"));
        gulp.watch("static/js/*.js", gulp.series("js"));
    })
);

gulp.task("default", gulp.series("browser-sync"));
