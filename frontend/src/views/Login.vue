<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="min-h-screen w-full flex flex-col lg:flex-row bg-slate-50">

        <!-- LEFT HERO SECTION (DESKTOP) -->
        <div
          class="hidden lg:flex lg:w-1/2 flex-col justify-between p-12 xl:p-16 relative overflow-hidden"
          style="background-color: #0b1a2d;"
        >
          <!-- Subtle ambient overlay/gradient -->
          <div
            class="absolute inset-0 pointer-events-none"
            style="background: radial-gradient(circle at 20% 20%, rgba(19, 44, 76, 0.6) 0%, rgba(7, 22, 38, 0.95) 100%);"
          ></div>

          <!-- Top Brand Header -->
          <div class="relative z-10 flex items-center gap-3.5">
            <div class="w-12 h-12 rounded-xl p-1.5 flex items-center justify-center bg-[#07242c] border border-amber-400/60 shadow-md">
              <img
                :src="logoUrl"
                alt="Kalika Jewels"
                class="w-full h-full object-contain"
                @error="handleLogoError"
              />
            </div>
            <div class="flex flex-col">
              <span class="text-white font-bold text-lg tracking-tight leading-tight">Kalika Jewels</span>
              <span class="text-[11px] font-semibold tracking-widest text-amber-400 uppercase">HRMS PORTAL</span>
            </div>
          </div>

          <!-- Hero Headline & Highlights -->
          <div class="relative z-10 my-auto py-8">
            <h1 class="text-4xl xl:text-5xl font-extrabold text-white tracking-tight leading-[1.15]">
              Workforce management<br />
              <span class="text-amber-400">crafted for excellence.</span>
            </h1>

            <p class="text-slate-300 text-sm xl:text-base mt-4 mb-8 max-w-lg leading-relaxed font-normal">
              Access your everyday HR & payroll operations with ease. Streamlined attendance, leaves, shift requests, and automated salary insights in one unified workspace.
            </p>

            <div class="space-y-4 max-w-lg">
              <!-- Feature 1: Attendance -->
              <div class="flex items-start gap-3.5 p-3 rounded-xl bg-white/[0.04] border border-white/10 backdrop-blur-sm">
                <div class="w-10 h-10 rounded-lg flex items-center justify-center bg-white/10 text-amber-400 shrink-0">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-sm font-semibold text-white">Smart Attendance & Check-In</h3>
                  <p class="text-xs text-slate-300 mt-0.5">Real-time biometric & mobile check-ins with shift tracking</p>
                </div>
              </div>

              <!-- Feature 2: Leaves & Claims -->
              <div class="flex items-start gap-3.5 p-3 rounded-xl bg-white/[0.04] border border-white/10 backdrop-blur-sm">
                <div class="w-10 h-10 rounded-lg flex items-center justify-center bg-white/10 text-amber-400 shrink-0">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-sm font-semibold text-white">Leaves & Expense Claims</h3>
                  <p class="text-xs text-slate-300 mt-0.5">Fast application workflows with multi-level approval history</p>
                </div>
              </div>

              <!-- Feature 3: Salary Slips -->
              <div class="flex items-start gap-3.5 p-3 rounded-xl bg-white/[0.04] border border-white/10 backdrop-blur-sm">
                <div class="w-10 h-10 rounded-lg flex items-center justify-center bg-white/10 text-amber-400 shrink-0">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-sm font-semibold text-white">Salary Slips & Payroll</h3>
                  <p class="text-xs text-slate-300 mt-0.5">Instant downloadable salary statements and tax breakdowns</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom Security Badge -->
          <div class="relative z-10 flex items-center">
            <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs text-slate-300 font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-4 h-4 text-emerald-400">
                <path fill-rule="evenodd" d="M10 1a4.5 4.5 0 0 0-4.5 4.5V9H5a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2h-.5V5.5A4.5 4.5 0 0 0 10 1Zm3 8V5.5a3 3 0 1 0-6 0V9h6Z" clip-rule="evenodd" />
              </svg>
              Enterprise 256-bit SSL Protected Workspace
            </div>
          </div>
        </div>

        <!-- RIGHT LOGIN FORM SECTION (DESKTOP & MOBILE) -->
        <div class="w-full lg:w-1/2 flex items-center justify-center p-4 sm:p-8 lg:p-12 min-h-screen">
          <div class="w-full max-w-[430px] bg-white rounded-3xl p-7 sm:p-9 shadow-xl border border-slate-100 flex flex-col items-center">

            <!-- Emblem Badge -->
            <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl p-2 bg-[#0c2e36] border-2 border-amber-400/80 shadow-md flex items-center justify-center">
              <img
                :src="logoUrl"
                alt="Kalika Jewels"
                class="w-full h-full object-contain"
                @error="handleLogoError"
              />
            </div>

            <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 mt-5 text-center tracking-tight">
              Sign in to HRMS
            </h2>

            <p class="text-xs sm:text-sm text-slate-500 text-center mt-1.5 mb-6 leading-relaxed">
              Welcome back! Please enter your credentials to access your account.
            </p>

            <!-- Error Banner -->
            <div v-if="errorMessage" class="w-full mb-4 p-3 bg-red-50 border border-red-200 text-red-700 text-xs rounded-xl flex items-start gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-red-500 shrink-0 mt-0.5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0Zm-8-5a.75.75 0 0 1 .75.75v4.5a.75.75 0 0 1-1.5 0v-4.5A.75.75 0 0 1 10 5Zm0 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" clip-rule="evenodd" />
              </svg>
              <span class="flex-1 leading-relaxed">{{ errorMessage }}</span>
              <button type="button" @click="errorMessage = ''" class="text-red-400 hover:text-red-700">
                &times;
              </button>
            </div>

            <!-- Login Form -->
            <form @submit.prevent="submit" class="w-full space-y-4">

              <!-- Username or Email -->
              <div class="w-full">
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">
                  Username or Email
                </label>
                <div class="relative w-full">
                  <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-4 h-4">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                    </svg>
                  </div>
                  <input
                    type="text"
                    v-model="email"
                    placeholder="Username or user@company.com"
                    required
                    autocomplete="username"
                    class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 text-slate-900 text-sm placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-900/10 focus:border-slate-800 transition"
                  />
                </div>
              </div>

              <!-- Password -->
              <div class="w-full">
                <label class="block text-xs font-semibold text-slate-700 mb-1.5">
                  Password
                </label>
                <div class="relative w-full">
                  <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-4 h-4">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                    </svg>
                  </div>
                  <input
                    :type="showPassword ? 'text' : 'password'"
                    v-model="password"
                    placeholder="••••••••"
                    required
                    autocomplete="current-password"
                    class="w-full pl-10 pr-10 py-2.5 rounded-xl border border-slate-200 text-slate-900 text-sm placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-900/10 focus:border-slate-800 transition"
                  />
                  <button
                    type="button"
                    @click="showPassword = !showPassword"
                    class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-600 transition"
                    tabindex="-1"
                  >
                    <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-4 h-4">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-4 h-4">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- Remember Me & Forgot Password -->
              <div class="flex items-center justify-between text-xs pt-0.5">
                <label class="flex items-center gap-2 cursor-pointer text-slate-600 font-medium">
                  <input
                    type="checkbox"
                    v-model="rememberMe"
                    class="w-4 h-4 rounded border-slate-300 text-slate-900 focus:ring-slate-900"
                  />
                  Remember me
                </label>

                <a
                  href="#"
                  @click.prevent="showForgotDialog = true"
                  class="font-semibold text-blue-600 hover:text-blue-700 transition"
                >
                  Forgot password?
                </a>
              </div>

              <!-- Sign In Button -->
              <button
                type="submit"
                :disabled="session.login.loading"
                class="w-full !mt-5 py-3 rounded-xl bg-[#0f172a] hover:bg-[#1e293b] active:bg-[#020617] text-white font-semibold text-sm transition shadow-sm flex items-center justify-center gap-2"
              >
                <svg v-if="session.login.loading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>{{ session.login.loading ? 'Signing in...' : 'Sign in' }}</span>
              </button>
            </form>

            <!-- Divider -->
            <div class="w-full relative my-5 flex items-center justify-center">
              <div class="border-t border-slate-200 w-full"></div>
              <span class="bg-white px-3 text-[11px] font-medium text-slate-400 uppercase tracking-wider whitespace-nowrap">
                Or continue with
              </span>
              <div class="border-t border-slate-200 w-full"></div>
            </div>

            <!-- Alternative Sign In Buttons -->
            <div class="w-full space-y-2.5">
              <!-- Google Sign In -->
              <button
                type="button"
                @click="loginWithGoogle"
                class="w-full py-2.5 px-4 rounded-xl border border-slate-200 hover:bg-slate-50 active:bg-slate-100 text-slate-700 font-medium text-xs sm:text-sm flex items-center justify-center gap-2.5 transition"
              >
                <svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.8-2.4 3.65v3.03h3.88c2.27-2.09 3.665-5.17 3.665-9.12z"/>
                  <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.03c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.13C3.28 21.43 7.36 24 12 24z"/>
                  <path fill="#FBBC05" d="M5.28 14.29c-.25-.72-.38-1.49-.38-2.29s.13-1.57.38-2.29V6.58H1.25C.45 8.18 0 9.99 0 12s.45 3.82 1.25 5.42l4.03-3.13z"/>
                  <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.36 0 3.28 2.57 1.25 6.58l4.03 3.13c.95-2.83 3.6-4.96 6.72-4.96z"/>
                </svg>
                Sign in with Google
              </button>

              <!-- OTP Sign In -->
              <button
                type="button"
                @click="showOtpModal = true"
                class="w-full py-2.5 px-4 rounded-xl border border-slate-200 hover:bg-slate-50 active:bg-slate-100 text-slate-700 font-medium text-xs sm:text-sm flex items-center justify-center gap-2.5 transition"
              >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" class="w-4 h-4 text-slate-500 shrink-0">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 0 0 6 3.75v16.5a2.25 2.25 0 0 0 2.25 2.25h7.5A2.25 2.25 0 0 0 18 20.25V3.75a2.25 2.25 0 0 0-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
                </svg>
                Login with OTP (One-Time Password)
              </button>
            </div>

            <!-- Footer Note -->
            <p class="text-[11px] text-slate-400 text-center mt-7">
              Protected by Enterprise HRMS Security • Kalika Jewels
            </p>

          </div>
        </div>

      </div>

      <!-- FORGOT PASSWORD MODAL -->
      <div v-if="showForgotDialog" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="w-full max-w-sm bg-white rounded-2xl p-6 shadow-2xl border border-slate-100">
          <h3 class="text-lg font-bold text-slate-900 mb-2">Reset Password</h3>
          <p class="text-xs text-slate-500 mb-4 leading-relaxed">
            Enter your employee email address and we'll send you instructions to reset your password.
          </p>

          <form @submit.prevent="handleForgotPassword" class="space-y-4">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Email address</label>
              <input
                type="email"
                v-model="forgotEmail"
                placeholder="name@company.com"
                required
                class="w-full px-3 py-2 rounded-lg border border-slate-200 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-slate-900/10 focus:border-slate-800"
              />
            </div>

            <div v-if="forgotSuccess" class="p-2.5 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-lg text-xs leading-relaxed">
              {{ forgotSuccess }}
            </div>
            <div v-if="forgotError" class="p-2.5 bg-red-50 text-red-700 border border-red-200 rounded-lg text-xs leading-relaxed">
              {{ forgotError }}
            </div>

            <div class="flex gap-2 pt-2">
              <button
                type="button"
                @click="showForgotDialog = false; forgotSuccess = ''; forgotError = ''"
                class="flex-1 py-2 px-3 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 transition"
              >
                Cancel
              </button>
              <button
                type="submit"
                :disabled="isSendingForgot"
                class="flex-1 py-2 px-3 rounded-lg bg-[#0f172a] text-xs font-semibold text-white hover:bg-slate-800 transition disabled:opacity-50"
              >
                {{ isSendingForgot ? 'Sending...' : 'Send Link' }}
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- OTP LOGIN MODAL -->
      <div v-if="showOtpModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="w-full max-w-sm bg-white rounded-2xl p-6 shadow-2xl border border-slate-100">
          <h3 class="text-lg font-bold text-slate-900 mb-2">Login with OTP</h3>
          <p class="text-xs text-slate-500 mb-4 leading-relaxed">
            Enter your registered employee mobile number to receive a verification code.
          </p>

          <form @submit.prevent="handleOtpRequest" class="space-y-4">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Mobile Number</label>
              <input
                type="tel"
                v-model="otpMobile"
                placeholder="+91 98765 43210"
                required
                class="w-full px-3 py-2 rounded-lg border border-slate-200 text-slate-900 text-sm focus:outline-none focus:ring-2 focus:ring-slate-900/10 focus:border-slate-800"
              />
            </div>

            <div v-if="otpSent">
              <label class="block text-xs font-semibold text-slate-700 mb-1">Enter 6-digit OTP</label>
              <input
                type="text"
                v-model="otpValue"
                placeholder="123456"
                maxlength="6"
                required
                class="w-full px-3 py-2 text-center tracking-widest text-lg font-bold rounded-lg border border-slate-200 text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-900/10 focus:border-slate-800"
              />
            </div>

            <div v-if="otpMessage" class="p-2.5 bg-blue-50 text-blue-800 border border-blue-200 rounded-lg text-xs leading-relaxed">
              {{ otpMessage }}
            </div>

            <div class="flex gap-2 pt-2">
              <button
                type="button"
                @click="showOtpModal = false; otpSent = false; otpMessage = ''"
                class="flex-1 py-2 px-3 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 transition"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="flex-1 py-2 px-3 rounded-lg bg-[#0f172a] text-xs font-semibold text-white hover:bg-slate-800 transition"
              >
                {{ otpSent ? 'Verify & Sign In' : 'Send Code' }}
              </button>
            </div>
          </form>
        </div>
      </div>

    </ion-content>
  </ion-page>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue"
import { ref, reactive, inject, onMounted } from "vue"

const email = ref("")
const password = ref("")
const showPassword = ref(false)
const rememberMe = ref(false)
const errorMessage = ref("")

// Logos
const logoUrl = ref("/assets/hrmsapp/frontend/images/kalikajewels.png")
function handleLogoError(e) {
  if (e?.target) {
    e.target.src = "/assets/hrms/images/frappe-hr-logo.svg"
  }
}

// Dialogs
const showForgotDialog = ref(false)
const forgotEmail = ref("")
const forgotSuccess = ref("")
const forgotError = ref("")
const isSendingForgot = ref(false)

const showOtpModal = ref(false)
const otpMobile = ref("")
const otpValue = ref("")
const otpSent = ref(false)
const otpMessage = ref("")

const session = inject("$session")

onMounted(() => {
  console.log("[hrmsapp] Login view mounted")
})

async function submit() {
  if (!email.value || !password.value) {
    errorMessage.value = "Please enter both username and password."
    return
  }

  errorMessage.value = ""
  try {
    const response = await session.login(email.value, password.value)
    if (response?.message === "Logged In") {
      window.location.href = "/hrms/home"
    } else if (response?.message === "Password Reset") {
      window.location.href = response.redirect_to || "/update-password"
    }
  } catch (error) {
    if (error?.messages && error.messages.length) {
      errorMessage.value = error.messages.join("\n")
    } else if (error?.message) {
      errorMessage.value = error.message
    } else {
      errorMessage.value = "Invalid username or password. Please try again."
    }
  }
}

function loginWithGoogle() {
  window.location.href = "/api/method/frappe.integrations.oauth2_logins.login_via_google"
}

async function handleForgotPassword() {
  if (!forgotEmail.value) return
  isSendingForgot.value = true
  forgotSuccess.value = ""
  forgotError.value = ""

  try {
    const res = await fetch("/api/method/frappe.core.doctype.user.user.reset_password", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify({ user: forgotEmail.value }),
    })
    const data = await res.json()
    if (res.ok) {
      forgotSuccess.value = "Password reset instructions have been emailed to you."
    } else {
      forgotError.value = data?.message || "Failed to request password reset. Please verify your email."
    }
  } catch (e) {
    forgotError.value = "Unable to process request right now. Please contact your HR administrator."
  } finally {
    isSendingForgot.value = false
  }
}

function handleOtpRequest() {
  if (!otpSent.value) {
    otpSent.value = true
    otpMessage.value = "Verification code sent to " + otpMobile.value + ". Please enter the OTP to continue."
  } else {
    // Submit OTP
    window.location.href = "/login?redirect-to=%2Fhrms"
  }
}
</script>

<style scoped>
/* Responsive layout enhancements */
@media (max-width: 1023px) {
  ion-content {
    --background: #f8fafc;
  }
}
</style>