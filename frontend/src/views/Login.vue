<template>
  <ion-page>
    <ion-content :fullscreen="true">
      
      <!-- MAIN BACKGROUND -->
      <div 
        class="min-h-screen flex items-center justify-center px-4 py-8 bg-cover bg-center relative"
        style="background-color: #051E24; background-image: url('/images/jewelry-bg.jpg');"
      >
        <!-- Dark overlay -->
        <div class="absolute inset-0 pointer-events-none" style="background-color: rgba(5, 30, 36, 0.75); mix-blend-mode: multiply;"></div>

        <!-- Centered Container -->
        <div class="w-full max-w-md mx-auto relative z-10 flex flex-col items-center">
          
          <!-- Glassmorphism Card -->
          <div class="w-full rounded-3xl px-6 py-5 sm:px-8 sm:py-6 shadow-2xl glass-card">
            
            <!-- Logo area -->
            <div class="flex flex-col items-center justify-center mb-6">
              <img
                :src="logoUrl"
                alt="Kalika Jewels"
                class="w-40 max-w-[170px] object-contain"
                @error="handleLogoError"
              />
            </div>

            <!-- Decorative Divider -->
            <div class="flex justify-center items-center mb-6">
               <div class="h-px w-full max-w-[100px] gradient-divider"></div>
               <div class="w-2 h-2 rotate-45 mx-2" style="background-color: #D4AF37;"></div>
               <div class="h-px w-full max-w-[100px] gradient-divider"></div>
            </div>

            <h2 class="text-2xl font-semibold text-center text-white mt-2 tracking-wide">
              Employee Login
            </h2>

            <p class="text-center text-sm mt-1 mb-5" style="color: #9ca3af;">
              Welcome back! Please login to continue
            </p>

            <!-- Login Form -->
            <form
              @submit.prevent="submit"
              class="space-y-4 px-2"
            >
              
              <!-- Employee ID Input -->
              <div class="w-full">
                <label class="flex items-center text-white text-sm mb-2 font-medium" style="padding-bottom: 6px;">
                  <!-- Hardcoded stroke color for SVG -->
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#D4AF37" class="w-4 h-4 mr-2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                  </svg>
                  Employee ID
                </label>
                <div class="relative w-full">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#9ca3af" class="w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                    </svg>
                  </div>
                  <input
                    type="text"
                    v-model="email"
                    placeholder="Enter your Employee ID"
                    class="w-full rounded-lg py-2.5 pl-10 pr-4 custom-input"
                  />
                </div>
              </div>

              <!-- Password Input -->
              <div class="w-full">
                <label class="flex items-center text-white text-sm mb-2 font-medium">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#D4AF37" class="w-4 h-4 mr-2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                  </svg>
                  Password
                </label>
                <div class="relative w-full">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#9ca3af" class="w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                    </svg>
                  </div>
                  <input
                    type="password"
                    v-model="password"
                    placeholder="Enter your password"
                    class="w-full rounded-lg py-3 pl-10 pr-10 custom-input"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center cursor-pointer icon-hover">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#9ca3af" class="w-5 h-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Remember Me & Forgot Password -->
              <div class="flex items-center justify-between text-sm mt-4 w-full">
                <label class="flex items-center cursor-pointer" style="color: #d1d5db;">
                  <input type="checkbox" class="mr-2 rounded border-gray-600 bg-transparent custom-checkbox">
                  Remember Me
                </label>
                <a href="#" class="transition-colors hover-white" style="color: #D4AF37;">
                  Forgot Password?
                </a>
              </div>

              <ErrorMessage :message="errorMessage" class="mt-4 w-full" style="color: #f87171;" />

              <!-- Primary Login Button -->
              <Button
                :loading="session.login.loading"
                class="w-full !mt-6 font-bold py-3 rounded-lg flex items-center justify-center border-0 btn-primary"
              >
                <div class="flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="#000000" class="w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                  </svg>
                  LOGIN
                </div>
              </Button>
              
              <!-- Divider -->
              <div class="flex items-center justify-center mt-6 mb-4 w-full">
                <div class="h-px w-full" style="background-color: rgba(75, 85, 99, 0.6);"></div>
                <span class="px-4 text-sm" style="color: #9ca3af;">OR</span>
                <div class="h-px w-full" style="background-color: rgba(75, 85, 99, 0.6);"></div>
              </div>

              <!-- Secondary OTP Button -->
              <button 
                type="button"
                @click="otp.showDialog = true" 
                class="w-full font-medium py-2.5 rounded-lg flex items-center justify-center btn-secondary"
              >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#D4AF37" class="w-5 h-5 mr-2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 0 1-1.043 3.296 3.745 3.745 0 0 1-3.296 1.043A3.745 3.745 0 0 1 12 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 0 1-3.296-1.043 3.745 3.745 0 0 1-1.043-3.296A3.745 3.745 0 0 1 3 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 0 1 1.043-3.296 3.746 3.746 0 0 1 3.296-1.043A3.746 3.746 0 0 1 12 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 0 1 3.296 1.043 3.746 3.746 0 0 1 1.043 3.296A3.745 3.745 0 0 1 21 12Z" />
                </svg>
                Login with OTP
              </button>

            </form>

            <!-- Card Footer text -->
            <div class="mt-6 mb-2 flex items-center justify-center text-[11px] w-full" style="color: #9ca3af;">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#6b7280" class="w-3.5 h-3.5 mr-1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 0 1-1.043 3.296 3.745 3.745 0 0 1-3.296 1.043A3.745 3.745 0 0 1 12 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 0 1-3.296-1.043 3.745 3.745 0 0 1-1.043-3.296A3.745 3.745 0 0 1 3 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 0 1 1.043-3.296 3.746 3.746 0 0 1 3.296-1.043A3.746 3.746 0 0 1 12 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 0 1 3.296 1.043 3.746 3.746 0 0 1 1.043 3.296A3.745 3.745 0 0 1 21 12Z" />
              </svg>
              Secure Access to Kalika Jewels System
            </div>

          </div>

          <!-- Copyright outside the card -->
          <div class="mt-6 text-center text-xs" style="color: #9ca3af;">
            © 2026 Kalika Jewels. All Rights Reserved.
          </div>

        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue"
import { inject, onMounted, reactive, ref } from "vue"
import { Button, ErrorMessage, createResource } from "frappe-ui"

const email = ref(null)
const password = ref(null)
const errorMessage = ref("")

const logoUrl = ref("/assets/hrmsapp/frontend/images/kalikajewels.png")

function handleLogoError(e) {
  if (e?.target) {
    e.target.src = "/assets/hrms/images/frappe-hr-logo.svg"
  }
}

const resetPassword = reactive({
  showDialog: false,
  link: "",
})

const otp = reactive({
  showDialog: false,
  tmp_id: "",
  code: "",
  verification: {},
})

const session = inject("$session")
const __ = inject("$translate")

onMounted(() => {
  console.log("[hrmsapp override] src_overrides/views/Login.vue mounted")
})

async function submit(e) {
  try {
    let response
    if (otp.showDialog) {
      response = await session.otp(otp.tmp_id, otp.code)
    } else {
      response = await session.login(email.value, password.value)
    }

    if (response.message === "Password Reset") {
      resetPassword.showDialog = true
      resetPassword.link = response.redirect_to
    } else {
      resetPassword.showDialog = false
      resetPassword.link = ""
    }

    // OTP verification
    if (response.verification) {
      if (response.verification.setup) {
        otp.showDialog = true
        otp.tmp_id = response.tmp_id
        otp.verification = response.verification
      } else {
        window.open("/login?redirect-to=" + encodeURIComponent(window.location.pathname), "_blank")
      }
    }
  } catch (error) {
    errorMessage.value = error.messages.join("\n")
  }
}

const user_pass_login_disabled = createResource({
  url: "hrms.api.system_settings.get_user_pass_login_disabled",
  method: 'GET',
  initialData: 1,
  auto: true,
})

const authProviders = createResource({
  url: "hrms.api.oauth.oauth_providers",
  auto: true,
})
</script>

<style scoped>
/* Fallback CSS to guarantee colors load properly regardless of Tailwind config */

.glass-card {
  background-color: rgba(10, 38, 45, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.4);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding-left: 24px;
  padding-right: 24px;
}

.gradient-divider {
  background: linear-gradient(to right, transparent, rgba(212, 175, 55, 0.5), transparent);
}

.custom-input {
  background-color: #05171B;
  border: 1px solid rgba(107, 114, 128, 0.5);
  color: #ffffff;
  transition: all 0.3s ease;
}

.custom-input::placeholder {
  color: #6b7280;
}

.custom-input:focus {
  outline: none;
  border-color: #D4AF37;
  box-shadow: 0 0 0 1px #D4AF37;
}

.btn-primary {
  background: linear-gradient(to right, #e8cf8d, #d7ae54, #c29636);
  color: #000000;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
  transition: opacity 0.3s;
}

.btn-primary:hover {
  opacity: 0.9;
}

.btn-secondary {
  background-color: rgba(5, 23, 27, 0.5);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: #D4AF37;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background-color: #05171B;
  border-color: #D4AF37;
}

.hover-white:hover {
  color: #ffffff !important;
}

.icon-hover:hover svg {
  stroke: #D4AF37;
}

.custom-checkbox:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.5);
}
</style>