#ifndef SkUserConfig_DEFINED
#define SkUserConfig_DEFINED

// For Linux at least, we want to match the most common ordering for our
// screen memory.  If we default to Skia's R-G-B-A ordering, we end up going
// down a very generic blit path in SDL (BlitNtoN).  This was taking 85% of
// the CPU in simple profiling.  We can do much better by using B-G-R-A
// ordering.  We will go down the much faster Blit4to4MaskAlpha.  This should
// still work ok as an OpenGL texture, as BGRA seems equally supported.
// We want this on all our platforms, it is the native window format.
#define SK_A32_SHIFT 24
#define SK_R32_SHIFT 16
#define SK_G32_SHIFT 8
#define SK_B32_SHIFT 0

#if defined(SK_BUILD_FOR_WIN32)

#define SK_BUILD_FOR_WIN

// VC8 doesn't support stdint.h, so we define those types here.
#define SK_IGNORE_STDINT_DOT_H
typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef short int16_t;
typedef unsigned short uint16_t;
typedef int int32_t;
typedef unsigned uint32_t;

// VC doesn't support __restrict__, so make it a NOP.
#undef SK_RESTRICT
#define SK_RESTRICT

#endif  // SK_BUILD_FOR_WIN32

#endif
