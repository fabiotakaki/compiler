var gulp = require('gulp');
// Requires the gulp-sass plugin
var sass = require('gulp-sass');

// Run tasks in sequence
var runSequence = require('run-sequence');

// Reload sync !!
var browserSync = require('browser-sync').create();

gulp.task('sass', function(){
  return gulp.src('app/assets/scss/**/*.scss')
    .pipe(sass()) // Using gulp-sass
    .pipe(gulp.dest('app/assets/css'))
    .pipe(browserSync.reload({
      stream: true
    }))
});

gulp.task('browserSync', function() {
  browserSync.init({
    server: {
      baseDir: 'app'
    },
  })
});

// watch sass files :)
gulp.task('watch', ['sass', 'browserSync'], function(){
  gulp.watch('app/assets/scss/**/*.scss', ['sass']); 
  gulp.watch('app/*.html', browserSync.reload); 
  gulp.watch('app/assets/js/**/*.js', browserSync.reload);
})

// default start !
gulp.task('default', function (callback) {
  runSequence(['sass','browserSync', 'watch'],
    callback
  )
})