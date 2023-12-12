import nodeResolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import babel from '@rollup/plugin-babel';
import replace from '@rollup/plugin-replace';
import excludeDependenciesFromBundle from "rollup-plugin-exclude-dependencies-from-bundle";

// https://www.codeguage.com/blog/setup-rollup-for-react

export default {
   input: 'src/apex_chart.jsx',
   output: {
      file: "../rectpy_apexcharts/bundle.js",
      format: "esm",
   },
   plugins: [
      nodeResolve({
         extensions: ['.js', '.jsx']
      }),
      babel({
         babelHelpers: 'bundled',
         presets: [
            ['@babel/preset-react'],
         //    [
         //       '@babel/preset-env',
         //       {
         //           targets: {
         //               esmodules: true,
         //           },
         //       },
         //   ],

         ],
         extensions: ['.js', '.jsx']
      }),
      commonjs(),
      replace({
         preventAssignment: false,
         'process.env.NODE_ENV': '"development"'
      }),
      // excludeDependenciesFromBundle({
      //   dependencies: true,
      //   dependencies: true
      // })
   ]
}