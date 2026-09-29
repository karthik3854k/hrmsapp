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
				class="flex flex-row items-center justify-between p-3.5 sm:p-4 hover:bg-white/[0.04] active:bg-white/[0.08] transition group outline-none"
				v-for="(link, idx) in props.items"
				:key="link.title"
				:to="{ name: link.route }"
			>
				<div class="flex flex-row items-center gap-3.5 grow">
					<div 
						class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 transition-transform group-hover:scale-105"
						:style="getIconBadgeStyle(link.title, idx)"
					>
						<component :is="link.icon" class="h-5 w-5" />
					</div>
					<div class="text-sm sm:text-base font-semibold text-white group-hover:text-[#D4AF37] transition">
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

function getIconBadgeStyle(title, idx) {
	const t = (title || "").toLowerCase()
	if (t.includes("attendance")) return { backgroundColor: "rgba(59, 130, 246, 0.25)", color: "#60a5fa", border: "1px solid rgba(59, 130, 246, 0.45)" }
	if (t.includes("shift")) return { backgroundColor: "rgba(168, 85, 247, 0.25)", color: "#c084fc", border: "1px solid rgba(168, 85, 247, 0.45)" }
	if (t.includes("leave")) return { backgroundColor: "rgba(245, 158, 11, 0.25)", color: "#fbbf24", border: "1px solid rgba(245, 158, 11, 0.45)" }
	if (t.includes("expense") || t.includes("claim")) return { backgroundColor: "rgba(16, 185, 129, 0.25)", color: "#34d399", border: "1px solid rgba(16, 185, 129, 0.45)" }
	if (t.includes("advance")) return { backgroundColor: "rgba(20, 184, 166, 0.25)", color: "#2dd4bf", border: "1px solid rgba(20, 184, 166, 0.45)" }
	if (t.includes("salary") || t.includes("slip")) return { backgroundColor: "rgba(212, 175, 55, 0.25)", color: "#F6E05E", border: "1px solid rgba(212, 175, 55, 0.5)" }

	const fallbacks = [
		{ backgroundColor: "rgba(59, 130, 246, 0.25)", color: "#60a5fa", border: "1px solid rgba(59, 130, 246, 0.45)" },
		{ backgroundColor: "rgba(168, 85, 247, 0.25)", color: "#c084fc", border: "1px solid rgba(168, 85, 247, 0.45)" },
		{ backgroundColor: "rgba(245, 158, 11, 0.25)", color: "#fbbf24", border: "1px solid rgba(245, 158, 11, 0.45)" },
		{ backgroundColor: "rgba(16, 185, 129, 0.25)", color: "#34d399", border: "1px solid rgba(16, 185, 129, 0.45)" },
		{ backgroundColor: "rgba(20, 184, 166, 0.25)", color: "#2dd4bf", border: "1px solid rgba(20, 184, 166, 0.45)" },
		{ backgroundColor: "rgba(212, 175, 55, 0.25)", color: "#F6E05E", border: "1px solid rgba(212, 175, 55, 0.5)" },
	]
	return fallbacks[idx % fallbacks.length]
}
</script>
