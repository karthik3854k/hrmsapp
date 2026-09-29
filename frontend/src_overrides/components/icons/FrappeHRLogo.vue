<template>
  <div class="flex items-center justify-center">
    <div class="w-12 h-12 rounded-xl p-1 bg-[#0b1a2d] border border-amber-400/60 shadow-md flex items-center justify-center">
      <img
        :src="logoUrl"
        alt="Kalika Jewels"
        class="w-full h-full object-contain"
        @error="handleLogoError"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const logoUrl = ref("/assets/hrmsapp/frontend/images/kalikajewels.png")

function handleLogoError(e) {
  if (e?.target) {
    e.target.src = "/assets/hrms/images/frappe-hr-logo.svg"
  }
}
</script>