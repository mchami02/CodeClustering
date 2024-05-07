
> sigma-examples@1.0.0 build
> npm run clean && ./build.js build


> sigma-examples@1.0.0 clean
> rimraf build


Building code-cluster...
[kotatsu] (v0.22.3)
[kotatsu] Compiling...
[kotatsu] {
  message: 'asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).\n' +
    'This can impact web performance.\n' +
    'Assets: \n' +
    '  bundle.js (2.93 MiB)',
  details: undefined,
  stack: 'AssetsOverSizeLimitWarning: asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).\n' +
    'This can impact web performance.\n' +
    'Assets: \n' +
    '  bundle.js (2.93 MiB)\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/performance/SizeLimitsPlugin.js:134:7\n' +
    '    at Hook.eval [as callAsync] (eval at create (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:9:1)\n' +
    '    at Hook.CALL_ASYNC_DELEGATE [as _callAsync] (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/Hook.js:18:14)\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/Compiler.js:864:27\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/neo-async/async.js:2818:7\n' +
    '    at done (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/neo-async/async.js:3522:9)\n' +
    '    at Hook.eval [as callAsync] (eval at create (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:6:1)\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/Compiler.js:718:33\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/graceful-fs/graceful-fs.js:143:16\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/graceful-fs/graceful-fs.js:61:14'
}
[kotatsu] {
  message: 'entrypoint size limit: The following entrypoint(s) combined asset size exceeds the recommended limit (244 KiB). This can impact web performance.\n' +
    'Entrypoints:\n' +
    '  main (2.93 MiB)\n' +
    '      bundle.js\n',
  details: undefined,
  stack: 'EntrypointsOverSizeLimitWarning: entrypoint size limit: The following entrypoint(s) combined asset size exceeds the recommended limit (244 KiB). This can impact web performance.\n' +
    'Entrypoints:\n' +
    '  main (2.93 MiB)\n' +
    '      bundle.js\n' +
    '\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/performance/SizeLimitsPlugin.js:139:7\n' +
    '    at Hook.eval [as callAsync] (eval at create (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:9:1)\n' +
    '    at Hook.CALL_ASYNC_DELEGATE [as _callAsync] (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/Hook.js:18:14)\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/Compiler.js:864:27\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/neo-async/async.js:2818:7\n' +
    '    at done (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/neo-async/async.js:3522:9)\n' +
    '    at Hook.eval [as callAsync] (eval at create (/Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:6:1)\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/webpack/lib/Compiler.js:718:33\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/graceful-fs/graceful-fs.js:143:16\n' +
    '    at /Users/mchami/ETH/AIResearch/SigmaCluster/examples/node_modules/graceful-fs/graceful-fs.js:61:14'
}
[kotatsu] Built in 17.2s.
[kotatsu] Done!

Finished building examples!
