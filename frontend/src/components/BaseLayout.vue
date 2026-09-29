<template>
	<ion-page>
		<ion-header class="ion-no-border">
			<div class="w-full bg-white border-b border-slate-100 shadow-sm">
				<div class="w-full max-w-xl mx-auto px-4 py-3 sm:py-3.5 flex flex-row justify-between items-center">
					<!-- Brand & Logo Above -->
					<div class="flex flex-row items-center gap-3">
						<div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl p-1 bg-[#0b1a2d] border border-amber-400/60 shadow-sm flex items-center justify-center shrink-0">
							<img
								:src="logoUrl"
								alt="Kalika Jewels"
								class="w-full h-full object-contain"
								@error="handleLogoError"
							/>
						</div>
						<div class="flex flex-col">
							<h2 class="text-base sm:text-lg font-bold text-slate-900 tracking-tight leading-tight">
								{{ props.pageTitle || __("Kalika Jewels") }}
							</h2>
							<span v-if="!props.pageTitle" class="text-[10px] font-semibold tracking-wider text-amber-600 uppercase leading-none">
								HRMS PORTAL
							</span>
						</div>
					</div>

					<!-- Header Actions (Notifications & Profile) -->
					<div class="flex flex-row items-center gap-3 ml-auto">
						<router-link
							:to="{ name: 'Notifications' }"
							v-slot="{ navigate }"
							class="flex flex-col items-center"
						>
							<span class="relative p-2 rounded-xl text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition cursor-pointer" @click="navigate">
								<FeatherIcon name="bell" class="h-5 w-5" />
								<span
									v-if="unreadNotificationsCount.data"
									class="absolute top-1.5 right-1.5 inline-block w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white shadow-sm"
								>
								</span>
							</span>
						</router-link>

						<router-link
							:to="{ name: 'Profile' }"
							class="flex flex-col items-center pl-1"
						>
							<div class="ring-2 ring-amber-400/40 rounded-full transition hover:ring-amber-500/70 p-0.5">
								<Avatar
									:image="user.data.user_image"
									:label="user.data.first_name"
									size="lg"
								/>
							</div>
						</router-link>
					</div>
				</div>
			</div>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="w-full min-h-screen bg-slate-50/60 pb-20">
				<div class="w-full max-w-xl mx-auto px-4">
					<slot name="body"></slot>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonHeader, IonContent, IonPage } from "@ionic/vue"
import { FeatherIcon, Avatar } from "frappe-ui"
import { unreadNotificationsCount } from "@/data/notifications"
import { inject, ref } from "vue"

const user = inject("$user")
const __ = inject("$translate")

const props = defineProps({
	pageTitle: {
		type: String,
		default: "",
	},
})

const logoUrl = ref("/assets/hrmsapp/frontend/images/kalikajewels.png")

function handleLogoError(e) {
	if (e?.target) {
		e.target.src = "/assets/hrms/images/frappe-hr-logo.svg"
	}
}
</script>

<style scoped>
ion-content {
	--background: #f8fafc;
}
</style>
