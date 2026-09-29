<template>
	<div class="flex flex-col gap-3 my-2 w-full">
		<div class="flex items-center justify-between px-1">
			<h3 class="text-base sm:text-lg font-bold text-white tracking-tight">
				{{ title || __("Quick Links") }}
			</h3>
			<span class="text-xs text-[#D4AF37] font-semibold tracking-wide uppercase">Frequent Services</span>
		</div>
		<div class="flex flex-col bg-[#07252c] rounded-2xl shadow-lg border border-[#D4AF37]/30 overflow-hidden divide-y divide-[#D4AF37]/15">
			<router-link
				class="flex flex-row items-center justify-between p-3.5 sm:p-4 hover:bg-white/[0.04] active:bg-white/[0.08] transition group"
				v-for="(link, idx) in props.items"
				:key="link.title"
				:to="{ name: link.route }"
			>
				<div class="flex flex-row items-center gap-3.5 grow">
					<div 
						class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0 transition-transform group-hover:scale-105"
						:class="getIconBadgeClass(link.title, idx)"
					>
						<component :is="link.icon" class="h-5 w-5" />
					</div>
					<div class="text-sm sm:text-base font-medium text-white group-hover:text-[#D4AF37] transition">
						{{ link.title }}
					</div>
				</div>
				<div class="w-7 h-7 rounded-full flex items-center justify-center text-[#D4AF37] group-hover:bg-white/10 transition">
					<FeatherIcon name="chevron-right" class="h-4 w-4" />
				</div>
			</router-link>
		</div>
	</div>
</template>

<script setup>
import { FeatherIcon } from "frappe-ui"

const props = defineProps({
	title: {
		type: String,
		required: false,
		default: "",
	},
	items: {
		type: Array,
		required: true,
	},
})

function getIconBadgeClass(title, idx) {
	const t = (title || "").toLowerCase()
	if (t.includes("attendance")) return "bg-blue-500/20 text-blue-300 border border-blue-500/30"
	if (t.includes("shift")) return "bg-purple-500/20 text-purple-300 border border-purple-500/30"
	if (t.includes("leave")) return "bg-amber-500/20 text-amber-300 border border-amber-500/30"
	if (t.includes("expense") || t.includes("claim")) return "bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
	if (t.includes("advance")) return "bg-teal-500/20 text-teal-300 border border-teal-500/30"
	if (t.includes("salary") || t.includes("slip")) return "bg-indigo-500/20 text-indigo-300 border border-indigo-500/30"

	const fallbacks = [
		"bg-blue-500/20 text-blue-300 border border-blue-500/30",
		"bg-purple-500/20 text-purple-300 border border-purple-500/30",
		"bg-amber-500/20 text-amber-300 border border-amber-500/30",
		"bg-emerald-500/20 text-emerald-300 border border-emerald-500/30",
		"bg-teal-500/20 text-teal-300 border border-teal-500/30",
		"bg-indigo-500/20 text-indigo-300 border border-indigo-500/30",
	]
	return fallbacks[idx % fallbacks.length]
}
</script>
