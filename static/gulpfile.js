'use strict'
let gulp = require('gulp');
let requireDir = require('require-dir');
requireDir('gulp-tasks');


gulp.paths = {
    dist: 'dist',
};

let paths = gulp.paths;

gulp.task('default', gulp.series('serve'));