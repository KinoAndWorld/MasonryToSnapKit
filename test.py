import sys

a = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -ivfsstatcache /Users/kino/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphoneos16.4-20E238-.sdkstatcache -target arm64-apple-ios15.2 -fmessage-length\\=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit\\=0 -std\\=gnu11 -fobjc-arc -fobjc-weak -fmodules -gmodules -fmodules-cache-path\\=/Users/kino/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -fmodules-prune-interval\\=86400 -fmodules-prune-after\\=345600 -fbuild-session-file\\=/Users/kino/Library/Developer/Xcode/DerivedData/ModuleCache.noindex/Session.modulevalidation -fmodules-validate-once-per-build-session -Wnon-modular-include-in-framework-module -Werror\\=non-modular-include-in-framework-module -Wno-trigraphs -fpascal-strings -O0 -fno-common -Wno-missing-field-initializers -Wno-missing-prototypes -Werror\\=return-type -Wdocumentation -Wunreachable-code -Wquoted-include-in-framework-header -Wno-implicit-atomic-properties -Werror\\=deprecated-objc-isa-usage -Wno-objc-interface-ivars -Werror\\=objc-root-class -Wno-arc-repeated-use-of-weak -Wimplicit-retain-self -Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body -Wuninitialized -Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion -Wno-float-conversion -Wnon-literal-null-conversion -Wobjc-literal-conversion -Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wundeclared-selector -Wdeprecated-implementations -Wno-implicit-fallthrough -DDEBUG\\=1 -DOBJC_OLD_DISPATCH_PROTOTYPES\\=0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.4.sdk -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -g -Wno-sign-conversion -Winfinite-recursion -Wcomma -Wblock-capture-autoreleasing -Wstrict-prototypes -Wno-semicolon-before-method-body -Wunguarded-availability -iquote /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/xxxxxxx-generated-files.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/xxxxxxx-own-target-headers.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/xxxxxxx-all-target-headers.hmap -iquote /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/xxxxxxx-project-headers.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Products/Debug-iphoneos/include -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/DerivedSources-normal/arm64 -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/DerivedSources/arm64 -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/DerivedSources -F/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Products/Debug-iphoneos -MMD -MT dependencies -MF /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.d --serialize-diagnostics /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.dia -c /Users/kino/Desktop/OCLintTestProj/xxxxxxx/xxxxxxx/Debug.m -o /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-bdztphfbiaehwufyzyxwmcggkuxp/Build/Intermediates.noindex/xxxxxxx.build/Debug-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.o"
b = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -target arm64-apple-ios15.2 -fmessage-length\\=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit\\=0 -std\\=gnu11 -fobjc-arc -fobjc-weak -fmodules -gmodules -fmodules-cache-path\\=/Users/kino/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -fmodules-prune-interval\\=86400 -fmodules-prune-after\\=345600 -fbuild-session-file\\=/Users/kino/Library/Developer/Xcode/DerivedData/ModuleCache.noindex/Session.modulevalidation -fmodules-validate-once-per-build-session -Wnon-modular-include-in-framework-module -Werror\\=non-modular-include-in-framework-module -Wno-trigraphs -fpascal-strings -Os -fno-common -Wno-missing-field-initializers -Wno-missing-prototypes -Werror\\=return-type -Wdocumentation -Wunreachable-code -Wquoted-include-in-framework-header -Wno-implicit-atomic-properties -Werror\\=deprecated-objc-isa-usage -Wno-objc-interface-ivars -Werror\\=objc-root-class -Wno-arc-repeated-use-of-weak -Wimplicit-retain-self -Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body -Wuninitialized -Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion -Wno-float-conversion -Wnon-literal-null-conversion -Wobjc-literal-conversion -Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wundeclared-selector -Wdeprecated-implementations -Wno-implicit-fallthrough -DNS_BLOCK_ASSERTIONS\\=1 -DOBJC_OLD_DISPATCH_PROTOTYPES\\=0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.1.sdk -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -g -fvisibility\\=hidden -Wno-sign-conversion -Winfinite-recursion -Wcomma -Wblock-capture-autoreleasing -Wstrict-prototypes -Wno-semicolon-before-method-body -Wunguarded-availability -iquote /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/xxxxxxx-generated-files.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/xxxxxxx-own-target-headers.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/xxxxxxx-all-target-headers.hmap -iquote /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/xxxxxxx-project-headers.hmap -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Products/Release-iphoneos/include -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/DerivedSources-normal/arm64 -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/DerivedSources/arm64 -I/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/DerivedSources -F/Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Products/Release-iphoneos -MMD -MT dependencies -MF /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.d --serialize-diagnostics /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.dia -c /Users/kino/Downloads/OCLintTestProj/xxxxxxx/xxxxxxx/Debug.m -o /Users/kino/Library/Developer/Xcode/DerivedData/xxxxxxx-fimbooifjywfcfemnylqjzjdcuyn/Build/Intermediates.noindex/xxxxxxx.build/Release-iphoneos/xxxxxxx.build/Objects-normal/arm64/Debug.o"

pars = a.split("-")
pars2 = b.split("-")

# 将列表转换为集合
set1 = set(pars)
set2 = set(pars2)

# 计算两个集合的差集
diff_set = set1.symmetric_difference(set2)

# 将差集转换为列表，并按行打印
for item in diff_set:
    print("-"+item)