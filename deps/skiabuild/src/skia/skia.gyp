# Copyright (c) 2010 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'skia',
      'type': '<(library)',
      'msvs_guid': 'CD9CA56E-4E94-444C-87D4-58CA1E6F300D',
      'sources': [
        #'../third_party/skia/src/animator/SkAnimate.h',
        #'../third_party/skia/src/animator/SkAnimateActive.cpp',
        #'../third_party/skia/src/animator/SkAnimateActive.h',
        #'../third_party/skia/src/animator/SkAnimateBase.cpp',
        #'../third_party/skia/src/animator/SkAnimateBase.h',
        #'../third_party/skia/src/animator/SkAnimateField.cpp',
        #'../third_party/skia/src/animator/SkAnimateMaker.cpp',
        #'../third_party/skia/src/animator/SkAnimateMaker.h',
        #'../third_party/skia/src/animator/SkAnimateProperties.h',
        #'../third_party/skia/src/animator/SkAnimateSchema.xsd',
        #'../third_party/skia/src/animator/SkAnimateSchema.xsx',
        #'../third_party/skia/src/animator/SkAnimateSet.cpp',
        #'../third_party/skia/src/animator/SkAnimateSet.h',
        #'../third_party/skia/src/animator/SkAnimator.cpp',
        #'../third_party/skia/src/animator/SkAnimatorScript.cpp',
        #'../third_party/skia/src/animator/SkAnimatorScript.h',
        #'../third_party/skia/src/animator/SkAnimatorScript2.cpp',
        #'../third_party/skia/src/animator/SkAnimatorScript2.h',
        #'../third_party/skia/src/animator/SkBase64.cpp',
        #'../third_party/skia/src/animator/SkBase64.h',
        #'../third_party/skia/src/animator/SkBoundable.cpp',
        #'../third_party/skia/src/animator/SkBoundable.h',
        #'../third_party/skia/src/animator/SkBuildCondensedInfo.cpp',
        #'../third_party/skia/src/animator/SkCondensedDebug.cpp',
        #'../third_party/skia/src/animator/SkCondensedRelease.cpp',
        #'../third_party/skia/src/animator/SkDisplayAdd.cpp',
        #'../third_party/skia/src/animator/SkDisplayAdd.h',
        #'../third_party/skia/src/animator/SkDisplayApply.cpp',
        #'../third_party/skia/src/animator/SkDisplayApply.h',
        #'../third_party/skia/src/animator/SkDisplayBounds.cpp',
        #'../third_party/skia/src/animator/SkDisplayBounds.h',
        #'../third_party/skia/src/animator/SkDisplayEvent.cpp',
        #'../third_party/skia/src/animator/SkDisplayEvent.h',
        #'../third_party/skia/src/animator/SkDisplayEvents.cpp',
        #'../third_party/skia/src/animator/SkDisplayEvents.h',
        #'../third_party/skia/src/animator/SkDisplayInclude.cpp',
        #'../third_party/skia/src/animator/SkDisplayInclude.h',
        #'../third_party/skia/src/animator/SkDisplayInput.cpp',
        #'../third_party/skia/src/animator/SkDisplayInput.h',
        #'../third_party/skia/src/animator/SkDisplayList.cpp',
        #'../third_party/skia/src/animator/SkDisplayList.h',
        #'../third_party/skia/src/animator/SkDisplayMath.cpp',
        #'../third_party/skia/src/animator/SkDisplayMath.h',
        #'../third_party/skia/src/animator/SkDisplayMovie.cpp',
        #'../third_party/skia/src/animator/SkDisplayMovie.h',
        #'../third_party/skia/src/animator/SkDisplayNumber.cpp',
        #'../third_party/skia/src/animator/SkDisplayNumber.h',
        #'../third_party/skia/src/animator/SkDisplayPost.cpp',
        #'../third_party/skia/src/animator/SkDisplayPost.h',
        #'../third_party/skia/src/animator/SkDisplayRandom.cpp',
        #'../third_party/skia/src/animator/SkDisplayRandom.h',
        #'../third_party/skia/src/animator/SkDisplayScreenplay.cpp',
        #'../third_party/skia/src/animator/SkDisplayScreenplay.h',
        #'../third_party/skia/src/animator/SkDisplayType.cpp',
        #'../third_party/skia/src/animator/SkDisplayType.h',
        #'../third_party/skia/src/animator/SkDisplayTypes.cpp',
        #'../third_party/skia/src/animator/SkDisplayTypes.h',
        #'../third_party/skia/src/animator/SkDisplayXMLParser.cpp',
        #'../third_party/skia/src/animator/SkDisplayXMLParser.h',
        #'../third_party/skia/src/animator/SkDisplayable.cpp',
        #'../third_party/skia/src/animator/SkDisplayable.h',
        #'../third_party/skia/src/animator/SkDraw3D.cpp',
        #'../third_party/skia/src/animator/SkDraw3D.h',
        #'../third_party/skia/src/animator/SkDrawBitmap.cpp',
        #'../third_party/skia/src/animator/SkDrawBitmap.h',
        #'../third_party/skia/src/animator/SkDrawBlur.cpp',
        #'../third_party/skia/src/animator/SkDrawBlur.h',
        #'../third_party/skia/src/animator/SkDrawClip.cpp',
        #'../third_party/skia/src/animator/SkDrawClip.h',
        #'../third_party/skia/src/animator/SkDrawColor.cpp',
        #'../third_party/skia/src/animator/SkDrawColor.h',
        #'../third_party/skia/src/animator/SkDrawDash.cpp',
        #'../third_party/skia/src/animator/SkDrawDash.h',
        #'../third_party/skia/src/animator/SkDrawDiscrete.cpp',
        #'../third_party/skia/src/animator/SkDrawDiscrete.h',
        #'../third_party/skia/src/animator/SkDrawEmboss.cpp',
        #'../third_party/skia/src/animator/SkDrawEmboss.h',
        #'../third_party/skia/src/animator/SkDrawExtraPathEffect.cpp',
        #'../third_party/skia/src/animator/SkDrawFull.cpp',
        #'../third_party/skia/src/animator/SkDrawFull.h',
        #'../third_party/skia/src/animator/SkDrawGradient.cpp',
        #'../third_party/skia/src/animator/SkDrawGradient.h',
        #'../third_party/skia/src/animator/SkDrawGroup.cpp',
        #'../third_party/skia/src/animator/SkDrawGroup.h',
        #'../third_party/skia/src/animator/SkDrawLine.cpp',
        #'../third_party/skia/src/animator/SkDrawLine.h',
        #'../third_party/skia/src/animator/SkDrawMatrix.cpp',
        #'../third_party/skia/src/animator/SkDrawMatrix.h',
        #'../third_party/skia/src/animator/SkDrawOval.cpp',
        #'../third_party/skia/src/animator/SkDrawOval.h',
        #'../third_party/skia/src/animator/SkDrawPaint.cpp',
        #'../third_party/skia/src/animator/SkDrawPaint.h',
        #'../third_party/skia/src/animator/SkDrawPath.cpp',
        #'../third_party/skia/src/animator/SkDrawPath.h',
        #'../third_party/skia/src/animator/SkDrawPoint.cpp',
        #'../third_party/skia/src/animator/SkDrawPoint.h',
        #'../third_party/skia/src/animator/SkDrawRectangle.cpp',
        #'../third_party/skia/src/animator/SkDrawRectangle.h',
        #'../third_party/skia/src/animator/SkDrawSaveLayer.cpp',
        #'../third_party/skia/src/animator/SkDrawSaveLayer.h',
        #'../third_party/skia/src/animator/SkDrawShader.cpp',
        #'../third_party/skia/src/animator/SkDrawShader.h',
        #'../third_party/skia/src/animator/SkDrawText.cpp',
        #'../third_party/skia/src/animator/SkDrawText.h',
        #'../third_party/skia/src/animator/SkDrawTextBox.cpp',
        #'../third_party/skia/src/animator/SkDrawTextBox.h',
        #'../third_party/skia/src/animator/SkDrawTo.cpp',
        #'../third_party/skia/src/animator/SkDrawTo.h',
        #'../third_party/skia/src/animator/SkDrawTransparentShader.cpp',
        #'../third_party/skia/src/animator/SkDrawTransparentShader.h',
        #'../third_party/skia/src/animator/SkDrawable.cpp',
        #'../third_party/skia/src/animator/SkDrawable.h',
        #'../third_party/skia/src/animator/SkDump.cpp',
        #'../third_party/skia/src/animator/SkDump.h',
        #'../third_party/skia/src/animator/SkExtraPathEffects.xsd',
        #'../third_party/skia/src/animator/SkExtras.h',
        #'../third_party/skia/src/animator/SkGetCondensedInfo.cpp',
        #'../third_party/skia/src/animator/SkHitClear.cpp',
        #'../third_party/skia/src/animator/SkHitClear.h',
        #'../third_party/skia/src/animator/SkHitTest.cpp',
        #'../third_party/skia/src/animator/SkHitTest.h',
        #'../third_party/skia/src/animator/SkIntArray.h',
        #'../third_party/skia/src/animator/SkMatrixParts.cpp',
        #'../third_party/skia/src/animator/SkMatrixParts.h',
        #'../third_party/skia/src/animator/SkMemberInfo.cpp',
        #'../third_party/skia/src/animator/SkMemberInfo.h',
        #'../third_party/skia/src/animator/SkOpArray.cpp',
        #'../third_party/skia/src/animator/SkOpArray.h',
        #'../third_party/skia/src/animator/SkOperand.h',
        #'../third_party/skia/src/animator/SkOperand2.h',
        #'../third_party/skia/src/animator/SkOperandInterpolator.h',
        #'../third_party/skia/src/animator/SkOperandIterpolator.cpp',
        #'../third_party/skia/src/animator/SkPaintParts.cpp',
        #'../third_party/skia/src/animator/SkPaintParts.h',
        #'../third_party/skia/src/animator/SkParseSVGPath.cpp',
        #'../third_party/skia/src/animator/SkPathParts.cpp',
        #'../third_party/skia/src/animator/SkPathParts.h',
        #'../third_party/skia/src/animator/SkPostParts.cpp',
        #'../third_party/skia/src/animator/SkPostParts.h',
        #'../third_party/skia/src/animator/SkScript.cpp',
        #'../third_party/skia/src/animator/SkScript.h',
        #'../third_party/skia/src/animator/SkScript2.h',
        #'../third_party/skia/src/animator/SkScriptCallBack.h',
        #'../third_party/skia/src/animator/SkScriptDecompile.cpp',
        #'../third_party/skia/src/animator/SkScriptRuntime.cpp',
        #'../third_party/skia/src/animator/SkScriptRuntime.h',
        #'../third_party/skia/src/animator/SkScriptTokenizer.cpp',
        #'../third_party/skia/src/animator/SkSnapshot.cpp',
        #'../third_party/skia/src/animator/SkSnapshot.h',
        #'../third_party/skia/src/animator/SkTDArray_Experimental.h',
        #'../third_party/skia/src/animator/SkTextOnPath.cpp',
        #'../third_party/skia/src/animator/SkTextOnPath.h',
        #'../third_party/skia/src/animator/SkTextToPath.cpp',
        #'../third_party/skia/src/animator/SkTextToPath.h',
        #'../third_party/skia/src/animator/SkTime.cpp',
        #'../third_party/skia/src/animator/SkTypedArray.cpp',
        #'../third_party/skia/src/animator/SkTypedArray.h',
        #'../third_party/skia/src/animator/SkXMLAnimatorWriter.cpp',
        #'../third_party/skia/src/animator/SkXMLAnimatorWriter.h',

        '../third_party/skia/src/core/ARGB32_Clamp_Bilinear_BitmapShader.h',
        '../third_party/skia/src/core/Sk64.cpp',
        '../third_party/skia/src/core/SkAlphaRuns.cpp',
        '../third_party/skia/src/core/SkAntiRun.h',
        '../third_party/skia/src/core/SkBitmap.cpp',
        '../third_party/skia/src/core/SkBitmapProcShader.cpp',
        '../third_party/skia/src/core/SkBitmapProcShader.h',
        '../third_party/skia/src/core/SkBitmapProcState.cpp',
        '../third_party/skia/src/core/SkBitmapProcState.h',
        '../third_party/skia/src/core/SkBitmapProcState_matrix.h',
        '../third_party/skia/src/core/SkBitmapProcState_matrixProcs.cpp',
        '../third_party/skia/src/core/SkBitmapProcState_sample.h',
        '../third_party/skia/src/core/SkBitmapSampler.cpp',
        '../third_party/skia/src/core/SkBitmapSampler.h',
        '../third_party/skia/src/core/SkBitmapSamplerTemplate.h',
        '../third_party/skia/src/core/SkBitmapShader16BilerpTemplate.h',
        '../third_party/skia/src/core/SkBitmapShaderTemplate.h',
        '../third_party/skia/src/core/SkBitmap_scroll.cpp',
        '../third_party/skia/src/core/SkBlitBWMaskTemplate.h',
        '../third_party/skia/src/core/SkBlitRow.h',
        '../third_party/skia/src/core/SkBlitRow_D16.cpp',
        '../third_party/skia/src/core/SkBlitRow_D32.cpp',
        '../third_party/skia/src/core/SkBlitRow_D4444.cpp',
        '../third_party/skia/src/core/SkBlitter.cpp',
        '../third_party/skia/src/core/SkBlitter_4444.cpp',
        '../third_party/skia/src/core/SkBlitter_A1.cpp',
        '../third_party/skia/src/core/SkBlitter_A8.cpp',
        '../third_party/skia/src/core/SkBlitter_ARGB32.cpp',
        '../third_party/skia/src/core/SkBlitter_RGB16.cpp',
        '../third_party/skia/src/core/SkBlitter_Sprite.cpp',
        '../third_party/skia/src/core/SkBuffer.cpp',
        '../third_party/skia/src/core/SkCanvas.cpp',
        '../third_party/skia/src/core/SkChunkAlloc.cpp',
        '../third_party/skia/src/core/SkColor.cpp',
        '../third_party/skia/src/core/SkColorFilter.cpp',
        '../third_party/skia/src/core/SkColorTable.cpp',
        '../third_party/skia/src/core/SkComposeShader.cpp',
        '../third_party/skia/src/core/SkConcaveToTriangles.cpp',
        '../third_party/skia/src/core/SkConcaveToTriangles.h',
        '../third_party/skia/src/core/SkCordic.cpp',
        '../third_party/skia/src/core/SkCordic.h',
        '../third_party/skia/src/core/SkCoreBlitters.h',
        '../third_party/skia/src/core/SkCubicClipper.cpp',
        '../third_party/skia/src/core/SkCubicClipper.h',
        '../third_party/skia/src/core/SkDebug.cpp',
        #'../third_party/skia/src/core/SkDebug_stdio.cpp',
        '../third_party/skia/src/core/SkDeque.cpp',
        '../third_party/skia/src/core/SkDevice.cpp',
        '../third_party/skia/src/core/SkDither.cpp',
        '../third_party/skia/src/core/SkDraw.cpp',
        '../third_party/skia/src/core/SkDrawProcs.h',
        #'../third_party/skia/src/core/SkDrawing.cpp',
        '../third_party/skia/src/core/SkEdgeBuilder.cpp',
        '../third_party/skia/src/core/SkEdgeClipper.cpp',
        '../third_party/skia/src/core/SkEdge.cpp',
        '../third_party/skia/src/core/SkEdge.h',
        '../third_party/skia/src/core/SkFP.h',
        '../third_party/skia/src/core/SkFilterProc.cpp',
        '../third_party/skia/src/core/SkFilterProc.h',
        '../third_party/skia/src/core/SkFlattenable.cpp',
        '../third_party/skia/src/core/SkFloat.cpp',
        '../third_party/skia/src/core/SkFloat.h',
        '../third_party/skia/src/core/SkFloatBits.cpp',
        '../third_party/skia/src/core/SkGeometry.cpp',
        '../third_party/skia/src/core/SkGlobals.cpp',
        '../third_party/skia/src/core/SkGlyphCache.cpp',
        '../third_party/skia/src/core/SkGlyphCache.h',
        '../third_party/skia/src/core/SkGraphics.cpp',
        '../third_party/skia/src/core/SkLineClipper.cpp',
        '../third_party/skia/src/core/SkMMapStream.cpp',
        '../third_party/skia/src/core/SkMallocPixelRef.cpp',
        '../third_party/skia/src/core/SkMask.cpp',
        '../third_party/skia/src/core/SkMaskFilter.cpp',
        '../third_party/skia/src/core/SkMath.cpp',
        '../third_party/skia/src/core/SkMatrix.cpp',
        '../third_party/skia/src/core/SkPackBits.cpp',
        '../third_party/skia/src/core/SkPaint.cpp',
        '../third_party/skia/src/core/SkPath.cpp',
        '../third_party/skia/src/core/SkPathEffect.cpp',
        '../third_party/skia/src/core/SkPathHeap.cpp',
        '../third_party/skia/src/core/SkPathHeap.h',
        '../third_party/skia/src/core/SkPathMeasure.cpp',
        '../third_party/skia/src/core/SkPicture.cpp',
        '../third_party/skia/src/core/SkPictureFlat.cpp',
        '../third_party/skia/src/core/SkPictureFlat.h',
        '../third_party/skia/src/core/SkPicturePlayback.cpp',
        '../third_party/skia/src/core/SkPicturePlayback.h',
        '../third_party/skia/src/core/SkPictureRecord.cpp',
        '../third_party/skia/src/core/SkPictureRecord.h',
        '../third_party/skia/src/core/SkPixelRef.cpp',
        '../third_party/skia/src/core/SkPoint.cpp',
        '../third_party/skia/src/core/SkProcSpriteBlitter.cpp',
        '../third_party/skia/src/core/SkPtrRecorder.cpp',
        '../third_party/skia/src/core/SkQuadClipper.cpp',
        '../third_party/skia/src/core/SkQuadClipper.h',
        '../third_party/skia/src/core/SkRasterizer.cpp',
        '../third_party/skia/src/core/SkRect.cpp',
        '../third_party/skia/src/core/SkRefCnt.cpp',
        '../third_party/skia/src/core/SkRegion.cpp',
        '../third_party/skia/src/core/SkRegionPriv.h',
        '../third_party/skia/src/core/SkRegion_path.cpp',
        '../third_party/skia/src/core/SkScalerContext.cpp',
        '../third_party/skia/src/core/SkScan.cpp',
        '../third_party/skia/src/core/SkScanPriv.h',
        '../third_party/skia/src/core/SkScan_AntiPath.cpp',
        '../third_party/skia/src/core/SkScan_Antihair.cpp',
        '../third_party/skia/src/core/SkScan_Hairline.cpp',
        '../third_party/skia/src/core/SkScan_Path.cpp',
        '../third_party/skia/src/core/SkShader.cpp',
        '../third_party/skia/src/core/SkShape.cpp',
        '../third_party/skia/src/core/SkSpriteBlitter_ARGB32.cpp',
        '../third_party/skia/src/core/SkSpriteBlitter_RGB16.cpp',
        '../third_party/skia/src/core/SkSinTable.h',
        '../third_party/skia/src/core/SkSpriteBlitter.h',
        '../third_party/skia/src/core/SkSpriteBlitterTemplate.h',
        '../third_party/skia/src/core/SkStream.cpp',
        '../third_party/skia/src/core/SkString.cpp',
        '../third_party/skia/src/core/SkStroke.cpp',
        '../third_party/skia/src/core/SkStrokerPriv.cpp',
        '../third_party/skia/src/core/SkStrokerPriv.h',
        '../third_party/skia/src/core/SkTSearch.cpp',
        '../third_party/skia/src/core/SkTSort.h',
        '../third_party/skia/src/core/SkTemplatesPriv.h',
        '../third_party/skia/src/core/SkTypeface.cpp',
        '../third_party/skia/src/core/SkUnPreMultiply.cpp',
        '../third_party/skia/src/core/SkUtils.cpp',
        '../third_party/skia/src/core/SkWriter32.cpp',
        '../third_party/skia/src/core/SkXfermode.cpp',

        '../third_party/skia/src/effects/Sk1DPathEffect.cpp',
        '../third_party/skia/src/effects/Sk2DPathEffect.cpp',
        '../third_party/skia/src/effects/SkAvoidXfermode.cpp',
        '../third_party/skia/src/effects/SkBlurDrawLooper.cpp',
        '../third_party/skia/src/effects/SkBlurMask.cpp',
        '../third_party/skia/src/effects/SkBlurMask.h',
        '../third_party/skia/src/effects/SkBlurMaskFilter.cpp',
        '../third_party/skia/src/effects/SkColorFilters.cpp',
        '../third_party/skia/src/effects/SkColorMatrixFilter.cpp',
        '../third_party/skia/src/effects/SkCornerPathEffect.cpp',
        '../third_party/skia/src/effects/SkDashPathEffect.cpp',
        '../third_party/skia/src/effects/SkDiscretePathEffect.cpp',
        '../third_party/skia/src/effects/SkEmbossMask.cpp',
        '../third_party/skia/src/effects/SkEmbossMask.h',
        '../third_party/skia/src/effects/SkEmbossMask_Table.h',
        '../third_party/skia/src/effects/SkEmbossMaskFilter.cpp',
        '../third_party/skia/src/effects/SkGradientShader.cpp',
        '../third_party/skia/src/effects/SkKernel33MaskFilter.cpp',
        '../third_party/skia/src/effects/SkLayerDrawLooper.cpp',
        '../third_party/skia/src/effects/SkLayerRasterizer.cpp',
        '../third_party/skia/src/effects/SkPaintFlagsDrawFilter.cpp',
        '../third_party/skia/src/effects/SkPorterDuff.cpp',
        '../third_party/skia/src/effects/SkPixelXorXfermode.cpp',
        '../third_party/skia/src/effects/SkRadialGradient_Table.h',
        '../third_party/skia/src/effects/SkTransparentShader.cpp',

        '../third_party/skia/src/images/bmpdecoderhelper.cpp',
        '../third_party/skia/src/images/bmpdecoderhelper.h',
        '../third_party/skia/src/images/fpdfemb.h',
        '../third_party/skia/src/images/fpdfemb_ext.h',
        '../third_party/skia/src/images/SkBitmap_RLEPixels.h',
        '../third_party/skia/src/images/SkCreateRLEPixelRef.cpp',
        #'../third_party/skia/src/images/SkFDStream.cpp',
        #'../third_party/skia/src/images/SkFlipPixelRef.cpp',
        '../third_party/skia/src/images/SkImageDecoder.cpp',
        '../third_party/skia/src/images/SkImageDecoder_Factory.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_fpdfemb.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libbmp.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libgif.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libico.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libjpeg.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libpng.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_libpvjpeg.cpp',
        #'../third_party/skia/src/images/SkImageDecoder_wbmp.cpp',
        #'../third_party/skia/src/images/SKImageEncoder.cpp',
        #'../third_party/skia/src/images/SKImageEncoder_Factory.cpp',
        #'../third_party/skia/src/images/SkImageRef.cpp',
        #'../third_party/skia/src/images/SkImageRefPool.cpp',
        #'../third_party/skia/src/images/SkImageRefPool.h',
        #'../third_party/skia/src/images/SkImageRef_GlobalPool.cpp',
        #'../third_party/skia/src/images/SkMovie.cpp',
        #'../third_party/skia/src/images/SkMovie_gif.cpp',
        '../third_party/skia/src/images/SkScaledBitmapSampler.cpp',
        '../third_party/skia/src/images/SkScaledBitmapSampler.h',

        '../third_party/skia/src/opts/opts_check_SSE2.cpp',

        #'../third_party/skia/src/ports/SkFontHost_FONTPATH.cpp',
        '../third_party/skia/src/ports/SkFontHost_FreeType.cpp',
        #'../third_party/skia/src/ports/SkFontHost_android.cpp',
        #'../third_party/skia/src/ports/SkFontHost_ascender.cpp',
        '../third_party/skia/src/ports/SkFontHost_tables.cpp',
        #'../third_party/skia/src/ports/SkFontHost_gamma.cpp',
        '../third_party/skia/src/ports/SkFontHost_gamma_none.cpp',
        #'../third_party/skia/src/ports/SkFontHost_linux.cpp',
        '../third_party/skia/src/ports/SkFontHost_mac.cpp',
        #'../third_party/skia/src/ports/SkFontHost_none.cpp',
        '../third_party/skia/src/ports/SkFontHost_win.cpp',
        '../third_party/skia/src/ports/SkGlobals_global.cpp',
        #'../third_party/skia/src/ports/SkImageDecoder_CG.cpp',
        #'../third_party/skia/src/ports/SkImageDecoder_empty.cpp',
        #'../third_party/skia/src/ports/SkImageRef_ashmem.cpp',
        #'../third_party/skia/src/ports/SkImageRef_ashmem.h',
        #'../third_party/skia/src/ports/SkOSEvent_android.cpp',
        #'../third_party/skia/src/ports/SkOSEvent_dummy.cpp',
        '../third_party/skia/src/ports/SkOSFile_stdio.cpp',
        #'../third_party/skia/src/ports/SkThread_none.cpp',
        #'../third_party/skia/src/ports/SkThread_pthread.cpp',
        '../third_party/skia/src/ports/SkThread_win.cpp',
        '../third_party/skia/src/ports/SkTime_Unix.cpp',
        #'../third_party/skia/src/ports/SkXMLParser_empty.cpp',
        #'../third_party/skia/src/ports/SkXMLParser_expat.cpp',
        #'../third_party/skia/src/ports/SkXMLParser_tinyxml.cpp',
        #'../third_party/skia/src/ports/SkXMLPullParser_expat.cpp',
        '../third_party/skia/src/ports/sk_predefined_gamma.h',

        '../third_party/skia/src/include/utils/mac/SkCGUtils.h',
        '../third_party/skia/src/utils/mac/SkCreateCGImageRef.cpp',

        '../third_party/skia/src/utils/SkParsePath.cpp',

        '../third_party/skia/include/core/Sk64.h',
        '../third_party/skia/include/core/SkAutoKern.h',
        '../third_party/skia/include/core/SkBitmap.h',
        '../third_party/skia/include/core/SkBlitter.h',
        '../third_party/skia/include/core/SkBounder.h',
        '../third_party/skia/include/core/SkBuffer.h',
        '../third_party/skia/include/core/SkCanvas.h',
        '../third_party/skia/include/core/SkChunkAlloc.h',
        '../third_party/skia/include/core/SkColor.h',
        '../third_party/skia/include/core/SkColorFilter.h',
        '../third_party/skia/include/core/SkColorPriv.h',
        '../third_party/skia/include/core/SkColorShader.h',
        '../third_party/skia/include/core/SkComposeShader.h',
        '../third_party/skia/include/core/SkDeque.h',
        '../third_party/skia/include/core/SkDescriptor.h',
        '../third_party/skia/include/core/SkDevice.h',
        '../third_party/skia/include/core/SkDither.h',
        '../third_party/skia/include/core/SkDraw.h',
        '../third_party/skia/include/core/SkDrawFilter.h',
        '../third_party/skia/include/core/SkDrawLooper.h',
        '../third_party/skia/include/core/SkDrawing.h',
        '../third_party/skia/include/core/SkEndian.h',
        '../third_party/skia/include/core/SkFDot6.h',
        '../third_party/skia/include/core/SkFixed.h',
        '../third_party/skia/include/core/SkFlattenable.h',
        '../third_party/skia/include/core/SkFloatBits.h',
        '../third_party/skia/include/core/SkFloatingPoint.h',
        '../third_party/skia/include/core/SkFontHost.h',
        '../third_party/skia/include/core/SkGeometry.h',
        '../third_party/skia/include/core/SkGlobals.h',
        '../third_party/skia/include/core/SkGraphics.h',
        '../third_party/skia/include/core/SkMMapStream.h',
        '../third_party/skia/include/core/SkMallocPixelRef.h',
        '../third_party/skia/include/core/SkMask.h',
        '../third_party/skia/include/core/SkMaskFilter.h',
        '../third_party/skia/include/core/SkMath.h',
        '../third_party/skia/include/core/SkMatrix.h',
        '../third_party/skia/include/core/SkOSFile.h',
        '../third_party/skia/include/core/SkPackBits.h',
        '../third_party/skia/include/core/SkPaint.h',
        '../third_party/skia/include/core/SkPath.h',
        '../third_party/skia/include/core/SkPathEffect.h',
        '../third_party/skia/include/core/SkPathMeasure.h',
        '../third_party/skia/include/core/SkPerspIter.h',
        '../third_party/skia/include/core/SkPicture.h',
        '../third_party/skia/include/core/SkPixelRef.h',
        '../third_party/skia/include/core/SkPoint.h',
        '../third_party/skia/include/core/SkPorterDuff.h',
        '../third_party/skia/include/core/SkPtrRecorder.h',
        '../third_party/skia/include/core/SkRandom.h',
        '../third_party/skia/include/core/SkRasterizer.h',
        '../third_party/skia/include/core/SkReader32.h',
        '../third_party/skia/include/core/SkRect.h',
        '../third_party/skia/include/core/SkRefCnt.h',
        '../third_party/skia/include/core/SkRegion.h',
        '../third_party/skia/include/core/SkScalar.h',
        '../third_party/skia/include/core/SkScalarCompare.h',
        '../third_party/skia/include/core/SkScalerContext.h',
        '../third_party/skia/include/core/SkScan.h',
        '../third_party/skia/include/core/SkShader.h',
        '../third_party/skia/include/core/SkStream.h',
        '../third_party/skia/include/core/SkString.h',
        '../third_party/skia/include/core/SkStroke.h',
        '../third_party/skia/include/core/SkTDArray.h',
        '../third_party/skia/include/core/SkTDStack.h',
        '../third_party/skia/include/core/SkTDict.h',
        '../third_party/skia/include/core/SkTRegistry.h',
        '../third_party/skia/include/core/SkTSearch.h',
        '../third_party/skia/include/core/SkTemplates.h',
        '../third_party/skia/include/core/SkThread.h',
        '../third_party/skia/include/core/SkThread_platform.h',
        '../third_party/skia/include/core/SkTime.h',
        '../third_party/skia/include/core/SkTypeface.h',
        '../third_party/skia/include/core/SkTypes.h',
        '../third_party/skia/include/core/SkUnPreMultiply.h',
        '../third_party/skia/include/core/SkUnitMapper.h',
        '../third_party/skia/include/core/SkUtils.h',
        '../third_party/skia/include/core/SkWriter32.h',
        '../third_party/skia/include/core/SkXfermode.h',

        '../third_party/skia/include/effects/Sk1DPathEffect.h',
        '../third_party/skia/include/effects/Sk2DPathEffect.h',
        '../third_party/skia/include/effects/SkAvoidXfermode.h',
        '../third_party/skia/include/effects/SkBlurDrawLooper.h',
        '../third_party/skia/include/effects/SkBlurMaskFilter.h',
        '../third_party/skia/include/effects/SkColorMatrix.h',
        '../third_party/skia/include/effects/SkColorMatrixFilter.h',
        '../third_party/skia/include/effects/SkCornerPathEffect.h',
        '../third_party/skia/include/effects/SkDashPathEffect.h',
        '../third_party/skia/include/effects/SkDiscretePathEffect.h',
        '../third_party/skia/include/effects/SkDrawExtraPathEffect.h',
        '../third_party/skia/include/effects/SkEmbossMaskFilter.h',
        '../third_party/skia/include/effects/SkGradientShader.h',
        '../third_party/skia/include/effects/SkKernel33MaskFilter.h',
        '../third_party/skia/include/effects/SkLayerDrawLooper.h',
        '../third_party/skia/include/effects/SkLayerRasterizer.h',
        '../third_party/skia/include/effects/SkNWayCanvas.h',
        '../third_party/skia/include/effects/SkPaintFlagsDrawFilter.h',
        '../third_party/skia/include/effects/SkPixelXorXfermode.h',
        '../third_party/skia/include/effects/SkTransparentShader.h',

        '../third_party/skia/include/ports/SkStream_Win.h',

        '../third_party/skia/include/images/SkFlipPixelRef.h',
        '../third_party/skia/include/images/SkImageDecoder.h',
        '../third_party/skia/include/images/SkImageEncoder.h',
        '../third_party/skia/include/images/SkImageRef.h',
        '../third_party/skia/include/images/SkImageRef_GlobalPool.h',
        '../third_party/skia/include/images/SkMovie.h',
        '../third_party/skia/include/images/SkPageFlipper.h',
      ],
      'include_dirs': [
        '..',
        'config',
        '../third_party/skia/include/config',
        '../third_party/skia/include/core',
        '../third_party/skia/include/effects',
        '../third_party/skia/include/images',
        '../third_party/skia/include/utils',
        '../third_party/skia/src/core',
      ],
      'msvs_disabled_warnings': [4244, 4267,4345, 4390, 4554, 4800],
      'mac_framework_dirs': [
        '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework/Frameworks',
      ],
      'defines': [
        'SK_BUILD_NO_IMAGE_ENCODE',
        'SK_USE_CORETEXT',
      ],
      'sources!': [
        '../third_party/skia/include/core/SkTypes.h',
      ],
      'conditions': [
        [ 'OS != "mac"', {
          'sources/': [
            ['exclude', '_mac\\.(cc|cpp|mm?)$'],
            ['exclude', '/mac/'] ],
        }],
        [ 'OS != "linux" and OS != "freebsd" and OS != "openbsd" and OS != "solaris"', {
          'sources/': [ ['exclude', '_(linux|gtk)\\.(cc|cpp)$'] ],
          'sources!': [
            '../third_party/skia/src/ports/SkFontHost_FreeType.cpp',
            '../third_party/skia/src/ports/SkFontHost_TryeType_Tables.cpp',
            '../third_party/skia/src/ports/SkFontHost_gamma_none.cpp',
            '../third_party/skia/src/ports/SkFontHost_gamma_none.cpp',
            '../third_party/skia/src/ports/SkFontHost_tables.cpp',
          ],
        }],
        [ 'OS != "win"', {
          'sources/': [ ['exclude', '_win\\.(cc|cpp)$'] ],
        }],
        [ 'armv7 == 1', {
          'defines': [
            '__ARM_ARCH__=7',
          ],
        }],
        [ 'armv7 == 1 and arm_neon == 1', {
          'defines': [
            '__ARM_HAVE_NEON',
          ],
        }],
        [ 'target_arch == "arm"', {
          'sources!': [
            '../third_party/skia/src/opts/opts_check_SSE2.cpp'
          ],
        }],
        ['clang==1', {
          'defines': [
            # Remove all use of __restrict__ -- skia uses it incorrectly,
            # and clang is more strict about it.
            # http://code.google.com/p/skia/issues/detail?id=63
            'SK_RESTRICT=',
          ],
        }],
        [ 'OS == "linux" or OS == "freebsd" or OS == "openbsd" or OS == "solaris"', {
          'dependencies': [
            '../build/linux/system.gyp:gdk',
            '../build/linux/system.gyp:fontconfig',
            '../build/linux/system.gyp:freetype2',
            '../third_party/harfbuzz/harfbuzz.gyp:harfbuzz',
            '../third_party/harfbuzz/harfbuzz.gyp:harfbuzz_interface',
            '../third_party/icu/icu.gyp:icuuc',
          ],
          'cflags': [
            '-Wno-unused',
            '-Wno-unused-function',
          ],
          'sources': [
            # http://code.google.com/p/chromium/wiki/LinuxSandboxIPC
            'ext/SkFontHost_fontconfig.cpp',
            'ext/SkFontHost_fontconfig_direct.cpp',
            'ext/SkFontHost_fontconfig_ipc.cpp',
            '../third_party/skia/src/core/SkBlitter_ARGB32_Subpixel.cpp',
            '../third_party/skia/src/ports/SkFontHost_FreeType_Subpixel.cpp',
            '../third_party/skia/src/core/SkFontHost.cpp',
          ],
          'export_dependent_settings': [
            '../third_party/harfbuzz/harfbuzz.gyp:harfbuzz',
            '../third_party/harfbuzz/harfbuzz.gyp:harfbuzz_interface',
          ],
          'defines': [
            'SK_SUPPORT_LCDTEXT',
          ],
        }],
        [ 'OS == "mac"', {
          'defines': [
            'SK_BUILD_FOR_MAC',
          ],
          'include_dirs': [
            '../third_party/skia/include/utils/mac',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
        }],
        [ 'OS == "win"', {
          'sources!': [
            '../third_party/skia/src/core/SkMMapStream.cpp',
            '../third_party/skia/src/ports/SkTime_Unix.cc',
            'ext/SkThread_chrome.cc',
          ],
          'include_dirs': [
            'config/win',
          ],
        },],
      ],
      'dependencies': [
        'skia_opts'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'config',
          '../third_party/skia/include/config',
          '../third_party/skia/include/core',
          '../third_party/skia/include/effects',
          'ext',
        ],
        'mac_framework_dirs': [
          '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework/Frameworks',
        ],
      },
    },

    # Due to an unfortunate intersection of lameness between gcc and gyp,
    # we have to build the *_SSE2.cpp files in a separate target.  The
    # gcc lameness is that, in order to compile SSE2 intrinsics code, it
    # must be passed the -msse2 flag.  However, with this flag, it may 
    # emit SSE2 instructions even for scalar code, such as the CPUID
    # test used to test for the presence of SSE2.  So that, and all other
    # code must be compiled *without* -msse2.  The gyp lameness is that it
    # does not allow file-specific CFLAGS, so we must create this extra
    # target for those files to be compiled with -msse2.
    #
    # This is actually only a problem on 32-bit Linux (all Intel Macs have
    # SSE2, Linux x86_64 has SSE2 by definition, and MSC will happily emit
    # SSE2 from instrinsics, which generating plain ol' 386 for everything
    # else).  However, to keep the .gyp file simple and avoid platform-specific
    # build breakage, we do this on all platforms.

    # For about the same reason, we need to compile the ARM opts files
    # separately as well.
    {
      'target_name': 'skia_opts',
      'type': '<(library)',
      'include_dirs': [
        '..',
        'config',
        '../third_party/skia/include/config',
        '../third_party/skia/include/core',
        '../third_party/skia/include/effects',
        '../third_party/skia/include/images',
        '../third_party/skia/include/utils',
        '../third_party/skia/src/core',
      ],
      'conditions': [
        [ '(OS == "linux" or OS == "freebsd" or OS == "openbsd") and target_arch != "arm"', {
          'cflags': [
            '-msse2',
          ],
        }],
        [ 'target_arch != "arm"', {
          'sources': [
            '../third_party/skia/src/opts/SkBitmapProcState_opts_SSE2.cpp',
            '../third_party/skia/src/opts/SkBlitRow_opts_SSE2.cpp',
            '../third_party/skia/src/opts/SkUtils_opts_SSE2.cpp',
          ],
        },
        {  # arm
          'conditions': [
            [ 'armv7 == 1', {
              'defines': [
                '__ARM_ARCH__=7',
              ],
            }],
            [ 'armv7 == 1 and arm_neon == 1', {
              'defines': [
                '__ARM_HAVE_NEON',
              ],
            }],
          ],
          # The assembly uses the frame pointer register (r7 in Thumb/r11 in
          # ARM), the compiler doesn't like that.
          'cflags': [
            '-fomit-frame-pointer',
          ],
          'sources': [
            '../third_party/skia/src/opts/SkBitmapProcState_opts_arm.cpp',
            '../third_party/skia/src/opts/SkBlitRow_opts_arm.cpp',
            '../third_party/skia/src/opts/SkUtils_opts_none.cpp',
          ],
        }],
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2: