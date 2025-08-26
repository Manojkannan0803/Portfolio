
Demo_model_ConstP
/*
 * File: ert_main.c
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

#include <stddef.h>
#include <stdio.h>            /* This example main program uses printf/fflush */
#include "Demo_model.h"                /* Model header file */

static RT_MODEL_Demo_model_T Demo_model_M_;
static RT_MODEL_Demo_model_T *const Demo_model_MPtr = &Demo_model_M_;/* Real-time model */
static DW_Demo_model_T Demo_model_DW;  /* Observable states */

/* '<Root>/setpoint' */
static real_T Demo_model_U_setpoint;

/* '<Root>/adjusted_setpoint' */
static real_T Demo_model_Y_adjusted_setpoint;

/*
 * Associating rt_OneStep with a real-time clock or interrupt service routine
 * is what makes the generated code "real-time".  The function rt_OneStep is
 * always associated with the base rate of the model.  Subrates are managed
 * by the base rate from inside the generated code.  Enabling/disabling
 * interrupts and floating point context switches are target specific.  This
 * example code indicates where these should take place relative to executing
 * the generated code step function.  Overrun behavior should be tailored to
 * your application needs.  This example simply sets an error status in the
 * real-time model and returns from rt_OneStep.
 */
void rt_OneStep(RT_MODEL_Demo_model_T *const Demo_model_M);
void rt_OneStep(RT_MODEL_Demo_model_T *const Demo_model_M)
{
  static boolean_T OverrunFlag = false;

  /* Disable interrupts here */

  /* Check for overrun */
  if (OverrunFlag) {
    return;
  }

  OverrunFlag = true;

  /* Save FPU context here (if necessary) */
  /* Re-enable timer or interrupt here */
  /* Set model inputs here */

  /* Step the model */
  Demo_model_step(Demo_model_M, Demo_model_U_setpoint,
                  &Demo_model_Y_adjusted_setpoint);

  /* Get model outputs here */

  /* Indicate task complete */
  OverrunFlag = false;

  /* Disable interrupts here */
  /* Restore FPU context here (if necessary) */
  /* Enable interrupts here */
}
has popup
