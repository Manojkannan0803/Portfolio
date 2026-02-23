/*
 * File: Setpoint_Adjuster_types.h
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

#ifndef Setpoint_Adjuster_types_h_
#define Setpoint_Adjuster_types_h_
#include "rtwtypes.h"
#ifndef DEFINED_TYPEDEF_FOR_Config_def_
#define DEFINED_TYPEDEF_FOR_Config_def_

typedef struct {
  real_T setpoints[3];
  real_T noise[3];
  real_T gain_matrix[9];
  boolean_T enable;
} Config_def;

#endif

#ifndef DEFINED_TYPEDEF_FOR_OutputBus_
#define DEFINED_TYPEDEF_FOR_OutputBus_

typedef struct {
  real_T adjusted_setpoint[3];
  int32_T status;
} OutputBus;

#endif

/* Forward declaration for rtModel */
typedef struct tag_RTM_Setpoint_Adjuster_T RT_MODEL_Setpoint_Adjuster_T;

#endif                                 /* Setpoint_Adjuster_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
