/*
 * File: Setpoint_Adjuster.h
 *
 * Code generated for Simulink model 'Setpoint_Adjuster'.
 *
 * Model version                  : 1.6
 * Simulink Coder version         : 24.2 (R2024b) 21-Jun-2024
 * C/C++ source code generated on : Sat Jan 31 14:56:25 2026
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef Setpoint_Adjuster_h_
#define Setpoint_Adjuster_h_
#ifndef Setpoint_Adjuster_COMMON_INCLUDES_
#define Setpoint_Adjuster_COMMON_INCLUDES_
#include "rtwtypes.h"
#endif                                 /* Setpoint_Adjuster_COMMON_INCLUDES_ */

#include "Setpoint_Adjuster_types.h"
#include "rt_defines.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Self model data, for system '<Root>' */
struct tag_RTM_Setpoint_Adjuster_T {
  const char_T * volatile errorStatus;
};

/* Model entry point functions */
extern void Setpoint_Adjuster_initialize(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M);
extern void Setpoint_Adjuster_terminate(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M);

/* Customized model step function */
extern void Setpoint_Adjuster_step(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M, Config_def *Setpoint_Adjuster_U_config_def, OutputBus
  *Setpoint_Adjuster_Y_output);

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
 * '<Root>' : 'Setpoint_Adjuster'
 * '<S1>'   : 'Setpoint_Adjuster/MATLAB Function'
 */
#endif                                 /* Setpoint_Adjuster_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
