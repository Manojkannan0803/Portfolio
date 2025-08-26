
Demo_model_ConstP
/*
 * File: Demo_model.h
 *
 * Code generated for Simulink model 'Demo_model'.
 *
 * Model version                  : 1.4
 * Simulink Coder version         : 24.2 (R2024b) 21-Jun-2024
 * C/C++ source code generated on : Tue Aug 26 11:53:32 2025
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef Demo_model_h_
#define Demo_model_h_
#ifndef Demo_model_COMMON_INCLUDES_
#define Demo_model_COMMON_INCLUDES_
#include "rtwtypes.h"
#endif                                 /* Demo_model_COMMON_INCLUDES_ */

#include "rtw_modelmap.h"
#include <string.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetDataMapInfo
#define rtmGetDataMapInfo(rtm)         ((rtm)->DataMapInfo)
#endif

#ifndef rtmSetDataMapInfo
#define rtmSetDataMapInfo(rtm, val)    ((rtm)->DataMapInfo = (val))
#endif

/* Forward declaration for rtModel */
typedef struct tag_RTM_Demo_model_T RT_MODEL_Demo_model_T;

#ifndef DEFINED_TYPEDEF_FOR_struct_hzTBusEv2u3nLXHohjpiIH_
#define DEFINED_TYPEDEF_FOR_struct_hzTBusEv2u3nLXHohjpiIH_

typedef struct {
  real_T gain;
  real_T offset;
} struct_hzTBusEv2u3nLXHohjpiIH;

#endif

#ifndef struct_tag_3tK9PV05vORUBt5Sj3q7EF
#define struct_tag_3tK9PV05vORUBt5Sj3q7EF

struct tag_3tK9PV05vORUBt5Sj3q7EF
{
  int32_T isInitialized;
  struct_hzTBusEv2u3nLXHohjpiIH config;
};

#endif                                 /* struct_tag_3tK9PV05vORUBt5Sj3q7EF */

#ifndef typedef_Demo_Demo_setpoint_adjuster_D_T
#define typedef_Demo_Demo_setpoint_adjuster_D_T

typedef struct tag_3tK9PV05vORUBt5Sj3q7EF Demo_Demo_setpoint_adjuster_D_T;

#endif                             /* typedef_Demo_Demo_setpoint_adjuster_D_T */

/* Block signals and states (default storage) for system '<Root>' */
typedef struct {
  Demo_Demo_setpoint_adjuster_D_T obj; /* '<Root>/Demo_setpoint_adjuster' */
} DW_Demo_model_T;

/* Constant parameters (default storage) */
typedef struct {
  /* Expression: Demo.getconfig
   * Referenced by: '<Root>/Demo_setpoint_adjuster'
   */
  struct_hzTBusEv2u3nLXHohjpiIH Demo_setpoint_adjuster_config;
} ConstP_Demo_model_T;

/* Real-time Model Data Structure */
struct tag_RTM_Demo_model_T {
  DW_Demo_model_T *dwork;

  /*
   * DataMapInfo:
   * The following substructure contains information regarding
   * structures generated in the model's C API.
   */
  struct {
    rtwCAPI_ModelMappingInfo mmi;
  } DataMapInfo;
};

/* Constant parameters (default storage) */
extern const ConstP_Demo_model_T Demo_model_ConstP;

/* Model entry point functions */
extern void Demo_model_initialize(RT_MODEL_Demo_model_T *const Demo_model_M,
  real_T *Demo_model_U_setpoint, real_T *Demo_model_Y_adjusted_setpoint);
extern void Demo_model_step(RT_MODEL_Demo_model_T *const Demo_model_M, real_T
  Demo_model_U_setpoint, real_T *Demo_model_Y_adjusted_setpoint);

/* Function to get C API Model Mapping Static Info */
extern const rtwCAPI_ModelMappingStaticInfo*
  Demo_model_GetCAPIStaticMap(void);

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'Demo_model'
 */
#endif                                 /* Demo_model_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
has popup
