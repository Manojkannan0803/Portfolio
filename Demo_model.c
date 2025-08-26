
Demo_model_ConstP
/*
 * File: Demo_model.c
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

#include "Demo_model.h"
#include "rtwtypes.h"
#include "Demo_model_capi.h"

/* Model step function */
void Demo_model_step(RT_MODEL_Demo_model_T *const Demo_model_M, real_T
                     Demo_model_U_setpoint, real_T
                     *Demo_model_Y_adjusted_setpoint)
{
  DW_Demo_model_T *Demo_model_DW = Demo_model_M->dwork;

  /* MATLABSystem: '<Root>/Demo_setpoint_adjuster' */
  if ((Demo_model_DW->obj.config.offset == 1.0E-13) &&
      (Demo_model_DW->obj.config.gain == 10.0)) {
  } else {
    Demo_model_DW->obj.config = Demo_model_ConstP.Demo_setpoint_adjuster_config;
  }

  /* Outport: '<Root>/adjusted_setpoint' incorporates:
   *  Inport: '<Root>/setpoint'
   *  MATLABSystem: '<Root>/Demo_setpoint_adjuster'
   * */
  /*  Default passthrough implementation */
  /*  Assign outputs */
  /*  TODO implement */
  *Demo_model_Y_adjusted_setpoint = Demo_model_U_setpoint
    * Demo_model_DW->obj.config.gain;
}

/* Model initialize function */
void Demo_model_initialize(RT_MODEL_Demo_model_T *const Demo_model_M, real_T
  *Demo_model_U_setpoint, real_T *Demo_model_Y_adjusted_setpoint)
{
  DW_Demo_model_T *Demo_model_DW = Demo_model_M->dwork;

  /* Registration code */

  /* states (dwork) */
  (void) memset((void *)Demo_model_DW, 0,
                sizeof(DW_Demo_model_T));

  /* external inputs */
  *Demo_model_U_setpoint = 0.0;

  /* external outputs */
  *Demo_model_Y_adjusted_setpoint = 0.0;

  /* Initialize DataMapInfo substructure containing ModelMap for C API */
  Demo_model_InitializeDataMapInfo(Demo_model_M);

  /* Start for MATLABSystem: '<Root>/Demo_setpoint_adjuster' */
  /*  Optionally initialize config/state here if needed */
  Demo_model_DW->obj.config = Demo_model_ConstP.Demo_setpoint_adjuster_config;
  Demo_model_DW->obj.isInitialized = 1;
}

has popup
