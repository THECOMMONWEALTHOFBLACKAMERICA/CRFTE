# CRTFE-HCM — Nonlinear Saturation Closure for the Near-Luminal Parametric Branch

**Date:** 10 September 2026  
**Status:** Reduced nonlinear theory. No hardware-amplitude prediction.

## Executive result

The linear Floquet model determines the onset of the anti-phase superluminal instability, but it does **not** determine a finite above-threshold field amplitude.

If the constitutive modulation is treated as an infinitely stiff prescribed pump, the linear unstable mode continues to grow exponentially. A finite steady state requires additional physics.

Three generic saturation mechanisms can regularize the growth:

1. finite pump energy / pump depletion;
2. amplitude-dependent detuning;
3. amplitude-dependent loss.

For equal-depth anti-phase modulation,

\[
m_e=m_m=m,\qquad \delta=\pi,
\]

the ideal resonant coupling is

\[
\gamma_0=\frac{mKc_m}{4}\sqrt{u^2-1}.
\]

With modal damping \(\Gamma_a,\Gamma_b\) and residual detuning \(\Delta\), the mode is unstable only if

\[
\boxed{
\gamma_0^2>
\Gamma_a\Gamma_b
\left[1+\frac{\Delta^2}{(\Gamma_a+\Gamma_b)^2}\right]
}.
\]

For equal modal quality factors \(Q_a=Q_b=Q\), this is equivalent to

\[
\boxed{m>m_{\rm th}=\sqrt{\frac{1}{Q^2}+4\left(\frac{\Delta}{\Omega}\right)^2}}.
\]

At zero detuning,

\[
\boxed{m_{\rm th}=1/Q}.
\]

For the V1 mathematical depth \(m=0.10\), the resonant threshold is \(Q>10\).

## Pump depletion

Introduce a finite pump amplitude \(p\):

\[
\dot a=-\Gamma_a a+g p\,b^*,
\]
\[
\dot b=-\Gamma_b b+g p\,a^*,
\]
\[
\dot p=F-\Gamma_p p-g_p ab.
\]

A nonzero steady signal/idler state requires

\[
g^2|p|^2=\Gamma_a\Gamma_b
\]

at zero detuning, so the participating pump clamps at

\[
\boxed{|p|_{\rm ss}=\frac{\sqrt{\Gamma_a\Gamma_b}}{|g|}}.
\]

If effective Floquet coupling is linear in modulation depth, the ideal modal-Q model gives

\[
\boxed{m_{\rm clamp}=\frac{1}{\sqrt{Q_aQ_b}}}.
\]

For equal \(Q\), \(m_{\rm clamp}=1/Q\).

Thus a finite, depletable pump can regularize the instability by transferring energy into the signal/idler pair until the participating pump returns to threshold. This mechanism is not present in the current prescribed-modulation linear model.

## Nonlinear detuning

If

\[
\Delta(I)=\Delta_0+\nu I,
\]

the growing field can shift itself away from the parametric crossing. Saturation occurs when

\[
\boxed{|
\Delta_{\rm sat}|=(\Gamma_a+\Gamma_b)\sqrt{\frac{\gamma_0^2}{\Gamma_a\Gamma_b}-1}}
\]

and, for equal modal \(Q\),

\[
\boxed{\frac{|\Delta_{\rm sat}|}{\Omega}=\frac12\sqrt{m^2-\frac1{Q^2}}}.
\]

For \(m=0.10\):

- \(Q=12\): about 2.76% of \(\Omega\) nonlinear detuning returns the system to threshold;
- \(Q=20\): about 4.33%;
- \(Q=50\): about 4.90%.

## Nonlinear loss

For

\[
\Gamma_a(I)=\Gamma_a+\beta I,\qquad
\Gamma_b(I)=\Gamma_b+\beta I,
\]

at zero detuning,

\[
\gamma_0^2=(\Gamma_a+\beta I)(\Gamma_b+\beta I)
\]

and

\[
\boxed{I_{\rm sat}=\frac{-(\Gamma_a+\Gamma_b)+\sqrt{(\Gamma_a-\Gamma_b)^2+4\gamma_0^2}}{2\beta}}.
\]

For equal damping,

\[
\boxed{I_{\rm sat}=\frac{\gamma_0-\Gamma}{\beta}}.
\]

## Reduced stability of the pump-depleted steady state

For the simplest symmetric resonant closure,

\[
\dot A=(gp-\Gamma)A,
\]
\[
\dot p=\Gamma_p(p_0-p)-g_pA^2,
\]

the nonzero fixed point has

\[
p_{\rm ss}=\Gamma/g,
\]

\[
A_{\rm ss}^2=\frac{\Gamma_p(p_0-\Gamma/g)}{g_p}.
\]

Linearization gives

\[
\lambda^2+\Gamma_p\lambda+2gg_pA_{\rm ss}^2=0.
\]

For positive \(\Gamma_p,g,g_p\), both eigenvalues have negative real part. The simplest finite-pump model therefore yields a stable saturated steady state, potentially approached through damped relaxation oscillations.

This does **not** establish hardware stability. Additional Floquet channels, thermal feedback, pump delay, component nonlinearities and higher-order effects can destabilize the state.

## Evidence boundary

The nonlinear analysis establishes that finite above-threshold operation is possible in principle once a physical saturation mechanism is introduced. It does not predict an absolute saturation field, power, gain, or efficiency.

Those quantities require measured or independently modeled nonlinear coefficients, pump-source impedance, frequency-dependent component Q, thermal response, and nonlinear constitutive behavior.
