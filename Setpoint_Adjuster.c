/*
 * File: Setpoint_Adjuster.c
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

#include "Setpoint_Adjuster.h"
#include "Setpoint_Adjuster_types.h"
#include <emmintrin.h>
#include <math.h>
#include "rtwtypes.h"

/* Model step function */
void Setpoint_Adjuster_step(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M, Config_def *Setpoint_Adjuster_U_config_def, OutputBus
  *Setpoint_Adjuster_Y_output)
{
  real_T c_y[3];
  real_T tmp_2[2];
  real_T tmp;
  real_T tmp_0;
  real_T tmp_1;
  int32_T k;
  boolean_T exitg1;
  boolean_T guard1;
  boolean_T y;

  /* MATLAB Function: '<Root>/MATLAB Function' incorporates:
   *  BusCreator generated from: '<Root>/MATLAB Function'
   *  Inport: '<Root>/config_def'
   */
  Setpoint_Adjuster_Y_output->adjusted_setpoint[0] = 0.0;
  Setpoint_Adjuster_Y_output->adjusted_setpoint[1] = 0.0;
  Setpoint_Adjuster_Y_output->adjusted_setpoint[2] = 0.0;
  if (!Setpoint_Adjuster_U_config_def->enable) {
    /* Outport: '<Root>/output' */
    Setpoint_Adjuster_Y_output->status = -1;
  } else {
    _mm_storeu_pd(&tmp_2[0], _mm_sub_pd(_mm_loadu_pd
      (&Setpoint_Adjuster_U_config_def->setpoints[0]), _mm_loadu_pd
      (&Setpoint_Adjuster_U_config_def->noise[0])));
    tmp = tmp_2[0];
    tmp_0 = tmp_2[1];
    tmp_1 = Setpoint_Adjuster_U_config_def->setpoints[2] -
      Setpoint_Adjuster_U_config_def->noise[2];
    for (k = 0; k <= 0; k += 2) {
      _mm_storeu_pd(&Setpoint_Adjuster_Y_output->adjusted_setpoint[k],
                    _mm_add_pd(_mm_add_pd(_mm_mul_pd(_mm_loadu_pd
        (&Setpoint_Adjuster_U_config_def->gain_matrix[k + 3]), _mm_set1_pd(tmp_0)),
        _mm_mul_pd(_mm_loadu_pd(&Setpoint_Adjuster_U_config_def->gain_matrix[k]),
                   _mm_set1_pd(tmp))), _mm_mul_pd(_mm_loadu_pd
        (&Setpoint_Adjuster_U_config_def->gain_matrix[k + 6]), _mm_set1_pd(tmp_1))));
    }

    for (k = 2; k < 3; k++) {
      Setpoint_Adjuster_Y_output->adjusted_setpoint[k] =
        (Setpoint_Adjuster_U_config_def->gain_matrix[k + 3] * tmp_0 +
         Setpoint_Adjuster_U_config_def->gain_matrix[k] * tmp) +
        Setpoint_Adjuster_U_config_def->gain_matrix[k + 6] * tmp_1;
    }

    y = false;
    k = 0;
    exitg1 = false;
    while ((!exitg1) && (k < 3)) {
      if (Setpoint_Adjuster_Y_output->adjusted_setpoint[k] < 0.0) {
        y = true;
        exitg1 = true;
      } else {
        k++;
      }
    }

    guard1 = false;
    if (y) {
      guard1 = true;
    } else {
      y = false;
      k = 0;
      exitg1 = false;
      while ((!exitg1) && (k < 3)) {
        if (Setpoint_Adjuster_Y_output->adjusted_setpoint[k] > 100.0) {
          y = true;
          exitg1 = true;
        } else {
          k++;
        }
      }

      if (y) {
        guard1 = true;
      } else {
        c_y[0] = fabs(Setpoint_Adjuster_U_config_def->noise[0]);
        c_y[1] = fabs(Setpoint_Adjuster_U_config_def->noise[1]);
        c_y[2] = fabs(Setpoint_Adjuster_U_config_def->noise[2]);
        y = false;
        k = 0;
        exitg1 = false;
        while ((!exitg1) && (k < 3)) {
          if (c_y[k] > 5.0) {
            y = true;
            exitg1 = true;
          } else {
            k++;
          }
        }

        /* Outport: '<Root>/output' */
        Setpoint_Adjuster_Y_output->status = y;
      }
    }

    if (guard1) {
      /* Outport: '<Root>/output' */
      Setpoint_Adjuster_Y_output->status = 2;
      Setpoint_Adjuster_Y_output->adjusted_setpoint[0] = fmax(0.0, fmin(100.0,
        Setpoint_Adjuster_Y_output->adjusted_setpoint[0]));
      Setpoint_Adjuster_Y_output->adjusted_setpoint[1] = fmax(0.0, fmin(100.0,
        Setpoint_Adjuster_Y_output->adjusted_setpoint[1]));
      Setpoint_Adjuster_Y_output->adjusted_setpoint[2] = fmax(0.0, fmin(100.0,
        Setpoint_Adjuster_Y_output->adjusted_setpoint[2]));
    }
  }

  /* End of MATLAB Function: '<Root>/MATLAB Function' */
  UNUSED_PARAMETER(Setpoint_Adjuster_M);
}

/* Model initialize function */
void Setpoint_Adjuster_initialize(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M)
{
  /* Registration code */
  {
    /* initialize error status */
    rtmSetErrorStatus(Setpoint_Adjuster_M, (NULL));
  }
}

/* Model terminate function */
void Setpoint_Adjuster_terminate(RT_MODEL_Setpoint_Adjuster_T *const
  Setpoint_Adjuster_M)
{
  /* (no terminate code required) */
  UNUSED_PARAMETER(Setpoint_Adjuster_M);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
